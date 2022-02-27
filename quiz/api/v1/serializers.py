from rest_framework.serializers import ModelSerializer

from accounts.api.v1.serializers import TeacherSerializer
from quiz.models import Quiz, Question


class QuizSerializer(ModelSerializer):
    teacher = TeacherSerializer(many=True)

    class Meta:
        model = Quiz
        fields = "__all__"


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
