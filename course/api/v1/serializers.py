from rest_framework import serializers

from course.models import Course, CourseCategory, Video, Blog, Comment


# noinspection PyMethodMayBeStatic
class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(many=True,queryset=Course.objects.all())
    student = serializers.PrimaryKeyRelatedField(many=True,queryset=Course.objects.all())

    class Meta:
        model = Course
        fields = '__all__'
        depth = 2


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
