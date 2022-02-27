from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from course.api.v1.serializers import CourseSerializer, CourseCategorySerializer
from course.models import Course, CourseCategory


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
