from django.urls import path
from .views import (
    QuestionListCreateAPIView,
    QuestionDetailAnswerAPIView,
    LikeAnswerAPIView,
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView,
)

urlpatterns = [
    path('questions/', QuestionListCreateAPIView.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', QuestionDetailAnswerAPIView.as_view(), name='question-detail-answer'),
    path('answers/<int:answer_id>/like/', LikeAnswerAPIView.as_view(), name='like-answer'),

    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]
