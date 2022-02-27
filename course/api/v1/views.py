from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from course.api.v1.serializers import CourseSerializer
from course.models import Course


# Course Model Crud

class CourseListCreateApiView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "id"
