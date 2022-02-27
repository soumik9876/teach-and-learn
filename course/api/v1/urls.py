from django.urls import path

from course.api.v1.views import CourseListCreateApiView, CourseRetrieveUpdateDestroyApiView, \
    CourseCategoryListCreateApiView, CourseCategoryRetrieveUpdateDestroyApiView, VideoListCreateApiView, \
    VideoRetrieveUpdateDestroyApiView, BlogListCreateApiView, BlogRetrieveUpdateDestroyApiView

urlpatterns = [
    path("course/", CourseListCreateApiView.as_view(), name="course-list-create"),
    path("course/<int:id>/", CourseRetrieveUpdateDestroyApiView.as_view(), name="course-retrieve-update-destroy"),

    path("course_category/", CourseCategoryListCreateApiView.as_view(), name="course-category-list-create"),
    path("course_category/<int:id>/", CourseCategoryRetrieveUpdateDestroyApiView.as_view(),
         name="course-category-retrieve-update-destroy"),

    path("video/", VideoListCreateApiView.as_view(), name="video-list-create"),
    path("video/<int:id>/", VideoRetrieveUpdateDestroyApiView.as_view(), name="video-retrieve-update-destroy"),

    path("blog/", BlogListCreateApiView.as_view(), name="blog-list-create"),
    path("video/<int:id>/", BlogRetrieveUpdateDestroyApiView.as_view(), name="blog-retrieve-update-destroy"),
]
