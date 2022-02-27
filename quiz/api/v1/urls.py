from django.urls import path

from quiz.api.v1.views import QuizListCreateAPIView, QuizRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('quiz/', QuizListCreateAPIView.as_view(), name="quiz-list-create"),
    path('quiz/<int:id>', QuizRetrieveUpdateDestroyAPIView.as_view(), name="quiz-retrieve-update-destroy"),
]
