from django.urls import path

from course.api.v1.views import CourseListCreateApiView, CourseRetrieveUpdateDestroyApiView

urlpatterns = [
    path("course/", CourseListCreateApiView.as_view(), name="course-list-create"),
    path("course/<int:id>/", CourseRetrieveUpdateDestroyApiView.as_view(), name="course-retrieve-update-destroy"),
]
