from rest_framework import serializers

from accounts.api.v1.serializers import TeacherSerializer, StudentSerializer
from accounts.models import Teacher, Student
from course.models import Course, CourseCategory, Video, Blog, Comment


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# noinspection PyMethodMayBeStatic
class CourseSerializer(serializers.ModelSerializer):
    from quiz.api.v1.serializers import QuizSerializer
    teacher = serializers.PrimaryKeyRelatedField(many=True, queryset=Teacher.objects.all(), write_only=True)
    teacher_list = serializers.SerializerMethodField(read_only=True)
    student = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all(), write_only=True,
                                                 required=False)
    student_list = serializers.SerializerMethodField(read_only=True)
    # category = serializers.PrimaryKeyRelatedField(queryset=CourseCategory.objects.all(), required=False)
    video_set = VideoSerializer(many=True, read_only=True)
    quiz_set = QuizSerializer(many=True, read_only=True)
    blog_set = BlogSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        depth = 2

    def get_teacher_list(self, obj):
        return TeacherSerializer(obj.teacher.all(), many=True).data

    def get_student_list(self, obj):
        return StudentSerializer(obj.student.all(), many=True).data
