from rest_framework.serializers import ModelSerializer

from accounts.api.v1.serializers import TeacherSerializer
from quiz.models import Quiz


class QuizSerializer(ModelSerializer):
    teacher = TeacherSerializer(many=True)

    class Meta:
        model = Quiz
        fields = "__all__"
