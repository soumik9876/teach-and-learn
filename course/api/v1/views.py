from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Student
from course.api.v1.serializers import CourseSerializer, CourseCategorySerializer, VideoSerializer, BlogSerializer, \
    CommentSerializer
from course.models import Course, CourseCategory, Video, Blog, Comment


# Course CRUD apis

class CourseListCreateApiView(ListCreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        search_text = self.request.GET.get('search_text', None)
        return Course.objects.filter(title__contains=search_text) if search_text else Course.objects.all()


class CourseRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "id"


# noinspection PyMethodMayBeStatic
class CourseJoinApi(APIView):
    def get(self, request, course_id):
        student = Student.objects.get_or_create(user=request.user)[0]
        Course.objects.get(id=course_id).student.add(student)
        context = {
            "result": "Successfully joined"
        }
        return Response(context, status=status.HTTP_200_OK)


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
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"


# Comment CRUD apis

class CommentListCreateApiView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"
