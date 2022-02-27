from rest_framework import serializers

from course.models import Course, CourseCategory, Video, Blog


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


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
