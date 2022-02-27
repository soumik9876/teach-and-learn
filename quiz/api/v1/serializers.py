from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.api.v1.serializers import TeacherSerializer
from quiz.models import Quiz, Question, Option, QuizResult


class QuizSerializer(ModelSerializer):
    teacher = TeacherSerializer(many=True)

    class Meta:
        model = Quiz
        fields = "__all__"


class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        exclude = ['created_date', 'modified_date']


class QuestionSerializer(ModelSerializer):
    options = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Question
        exclude = ['created_date', 'modified_date']

    def get_options(self, obj):
        data = OptionSerializer(obj.option_set.all(), many=True).data
        return data


class QuizResultSerializer(ModelSerializer):
    total_marks = serializers.IntegerField(read_only=True)

    class Meta:
        model = QuizResult
        fields = "__all__"
