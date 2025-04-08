from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Question, Answer, Like
from .serializers import QuestionSerializer, AnswerSerializer, RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class QuestionListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        questions = Question.objects.all().order_by('-created_at')
        serializer = QuestionSerializer(questions, many=True)
        return Response({"message": "Questions fetched", "result": serializer.data, "error": False})

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "Question posted", "result": serializer.data, "error": False}, status=201)
        return Response({"message": "Post failed", "result": serializer.errors, "error": True}, status=400)

class QuestionDetailAnswerAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response({"message": f"Question not found with id {pk}", "result": {}, "error": True}, status=404)
        question_data = QuestionSerializer(question).data
        answers = AnswerSerializer(question.answers.all(), many=True).data
        return Response({"message": "Fetched", "result": {"question": question_data, "answers": answers}, "error": False})

    def post(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response({"message": f"Question not found with id {pk}", "result": {}, "error": True}, status=404)
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, question=question)
            return Response({"message": "Answer added", "result": serializer.data, "error": False}, status=201)
        return Response({"message": "Answer failed", "result": serializer.errors, "error": True}, status=400)

class LikeAnswerAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, answer_id):
        try:
            answer = Answer.objects.get(pk=answer_id)
        except Answer.DoesNotExist:
            return Response({"message": f"Answer not found with id {answer_id}", "result": {}, "error": True}, status=404)
        Like.objects.get_or_create(user=request.user, answer=answer)
        return Response({"message": "Answer liked", "result": {"answer_id": answer_id}, "error": False})

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Registered",
                "result": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "username": user.username
                },
                "error": False
            }, status=201)
        return Response({"message": "Register failed", "result": serializer.errors, "error": True}, status=400)

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Login successful",
                "result": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "username": user.username
                },
                "error": False
            })
        return Response({"message": "Invalid credentials", "result": {}, "error": True}, status=401)

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful", "result": {}, "error": False})