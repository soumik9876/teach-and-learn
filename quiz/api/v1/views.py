from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from quiz.api.v1.serializers import QuizSerializer, QuestionSerializer, OptionSerializer, QuizResultSerializer
from quiz.models import Quiz, Question, Option, QuizResult


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


class OptionListCreateAPIView(ListCreateAPIView):
    serializer_class = OptionSerializer
    queryset = Option.objects.all()


class OptionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OptionSerializer
    queryset = Option.objects.all()
    lookup_field = "id"


class QuizResultListCreateAPIView(ListCreateAPIView):
    serializer_class = QuizResultSerializer
    queryset = QuizResult.objects.all()


class QuizResultRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuizResultSerializer
    queryset = QuizResult.objects.all()
    lookup_field = "id"
