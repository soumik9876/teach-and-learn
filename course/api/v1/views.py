from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from course.api.v1.serializers import CourseSerializer, CourseCategorySerializer, VideoSerializer, BlogSerializer
from course.models import Course, CourseCategory, Video, Blog


# Course CRUD apis

class CourseListCreateApiView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "id"


# CourseCategorySerializer CRUD apis

class CourseCategoryListCreateApiView(ListCreateAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer


class CourseCategoryRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer
    lookup_field = "id"


# Video CRUD apis

class VideoListCreateApiView(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = "id"


# Blog CRUD apis

class BlogListCreateApiView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = "id"
