from django.urls import path

from quiz.api.v1.views import QuizListCreateAPIView, QuizRetrieveUpdateDestroyAPIView, QuestionListCreateAPIView, \
    QuestionRetrieveUpdateDestroyAPIView, OptionListCreateAPIView, OptionRetrieveUpdateDestroyAPIView, \
    QuizResultListCreateAPIView, QuizResultRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('quiz/', QuizListCreateAPIView.as_view(), name="quiz-list-create"),
    path('quiz/<int:id>', QuizRetrieveUpdateDestroyAPIView.as_view(), name="quiz-retrieve-update-destroy"),
    path('question/', QuestionListCreateAPIView.as_view(), name="question-list-create"),
    path('question/<int:id>/', QuestionRetrieveUpdateDestroyAPIView.as_view(), name="question-retrieve-update-destroy"),
    path('option/', OptionListCreateAPIView.as_view(), name="option-list-create"),
    path('option/<int:id>', OptionRetrieveUpdateDestroyAPIView.as_view(), name="option-retrieve-update-destroy"),
    path('quiz-result/', QuizResultListCreateAPIView.as_view(), name="quiz-result-list-create"),
    path('quiz-result/<int:id>', QuizResultRetrieveUpdateDestroyAPIView.as_view(),
         name="quiz-result-retrieve-update-destroy"),
]
