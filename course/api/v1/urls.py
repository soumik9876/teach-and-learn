from django.urls import path

from course.api.v1.views import CourseListCreateApiView, CourseRetrieveUpdateDestroyApiView, \
    CourseCategoryListCreateApiView, CourseCategoryRetrieveUpdateDestroyApiView

urlpatterns = [
    path("course/", CourseListCreateApiView.as_view(), name="course-list-create"),
    path("course/<int:id>/", CourseRetrieveUpdateDestroyApiView.as_view(), name="course-retrieve-update-destroy"),

    path("course_category/", CourseCategoryListCreateApiView.as_view(), name="course-category-list-create"),
    path("course_category/<int:id>/", CourseCategoryRetrieveUpdateDestroyApiView.as_view(),
         name="course-category-list-create"),
]
