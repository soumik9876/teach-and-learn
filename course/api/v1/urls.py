from django.urls import path

from course.api.v1.views import CourseListCreateApiView

urlpatterns = [
    path("courses/", CourseListCreateApiView.as_view(), name="course-list-create")
]
