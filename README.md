# Quora Clone API

## Overview
The Quora Clone API is a simplified version of the Quora platform, allowing users to register/login, post questions, answer them, like answers, and view a feed of content. It uses Django and Django Rest Framework (DRF) with class-based views and custom response formats.

## 🔧 Installation

### Clone the repository:
```bash
git clone https://github.com/your-username/quora_clone.git
cd quora_clone
```

### Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Apply migrations:
```bash
python manage.py migrate
```

### Run the development server:
```bash
python manage.py runserver
```

## 🔗 API Endpoints

### 1. User Login
**Endpoint:** `POST /login/`

**Request Body:**
```json
{
  "username": "johndoe",
  "password": "password123"
}
```

**Response:**
```json
{
  "message": "Login successful",
  "result": {"token": "<auth_token>", "user": {"id": 1, "username": "johndoe"}},
  "error": false
}
```

---

### 2. Post a Question
**Endpoint:** `POST /questions/`

**Request Body:**
```json
{
  "title": "What is Django?",
  "content": "Can someone explain Django framework?"
}
```

**Response:**
```json
{
  "message": "Question posted successfully",
  "result": {
    "id": 1,
    "title": "What is Django?",
    "content": "Can someone explain Django framework?",
    "user": 1
  },
  "error": false
}
```

---

### 3. View All Questions
**Endpoint:** `GET /questions/`

**Response:**
```json
{
  "message": "Questions retrieved successfully",
  "result": [
    {
      "id": 1,
      "title": "What is Django?",
      "content": "Can someone explain Django framework?",
      "user": 1
    }
  ],
  "error": false
}
```

---

### 4. Post an Answer
**Endpoint:** `POST /questions/{id}/answer/`

**Request Body:**
```json
{
  "content": "Django is a high-level Python web framework."
}
```

**Response:**
```json
{
  "message": "Answer posted successfully",
  "result": {
    "id": 1,
    "question": 1,
    "content": "Django is a high-level Python web framework.",
    "user": 1
  },
  "error": false
}
```

---

### 5. Like an Answer
**Endpoint:** `POST /answers/{id}/like/`

**Response:**
```json
{
  "message": "Answer liked successfully",
  "result": {},
  "error": false
}
```

---

### 6. Logout
**Endpoint:** `POST /logout/`

**Response:**
```json
{
  "message": "Logout successful",
  "result": {},
  "error": false
}
```

## 🧩 Models Overview
- **User**: Custom User model with username, email, password
- **Question**: Stores question title and content with user reference
- **Answer**: Stores answers with foreign key to question and user
- **Like**: Tracks which user liked which answer

## 🔁 URL Patterns
```python
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('questions/', QuestionListCreateView.as_view(), name='questions'),
    path('questions/<int:pk>/answer/', AnswerCreateView.as_view(), name='answer'),
    path('answers/<int:pk>/like/', LikeAnswerView.as_view(), name='like-answer'),
]
```

## ▶️ Running
To run the development server:
```bash
python manage.py runserver
```

---


