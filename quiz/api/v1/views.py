from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from quiz.api.v1.serializers import QuizSerializer
from quiz.models import Quiz


class QuizListCreateAPIView(ListCreateAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class QuizRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    lookup_field = "id"
