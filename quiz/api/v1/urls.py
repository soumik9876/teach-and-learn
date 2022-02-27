from django.urls import path

from quiz.api.v1.views import QuizListCreateAPIView, QuizRetrieveUpdateDestroyAPIView, QuestionListCreateAPIView, \
    QuestionRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('quiz/', QuizListCreateAPIView.as_view(), name="quiz-list-create"),
    path('quiz/<int:id>', QuizRetrieveUpdateDestroyAPIView.as_view(), name="quiz-retrieve-update-destroy"),
    path('question/', QuestionListCreateAPIView.as_view(), name="question-list-create"),
    path('question/<int:id>/', QuestionRetrieveUpdateDestroyAPIView.as_view(), name="question-retrieve-update-destroy")
]
