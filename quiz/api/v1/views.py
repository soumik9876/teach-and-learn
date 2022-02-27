from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from quiz.api.v1.serializers import QuizSerializer, QuestionSerializer
from quiz.models import Quiz, Question


class QuizListCreateAPIView(ListCreateAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class QuizRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    lookup_field = "id"


class QuestionListCreateAPIView(ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = "id"



