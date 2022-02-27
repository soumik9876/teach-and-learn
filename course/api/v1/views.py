from rest_framework.generics import ListCreateAPIView

from course.api.v1.serializers import CourseSerializer
from course.models import Course


class CourseListCreateApiView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
