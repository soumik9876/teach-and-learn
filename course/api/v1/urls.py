from django.urls import path

from course.api.v1.views import CourseListCreateApiView, CourseRetrieveUpdateDestroyApiView, \
    CourseCategoryListCreateApiView, CourseCategoryRetrieveUpdateDestroyApiView, VideoListCreateApiView, \
    VideoRetrieveUpdateDestroyApiView, BlogListCreateApiView, BlogRetrieveUpdateDestroyApiView, \
    CommentListCreateApiView, CommentRetrieveUpdateDestroyApiView, CourseJoinApi, SSLCommerzSessionAPI, \
    IPNVerifyAPIView, ProductRedirectView, PersonalCoursesListAPIView

urlpatterns = [
    path("course/", CourseListCreateApiView.as_view(), name="course-list-create"),
    path("course/<int:id>/", CourseRetrieveUpdateDestroyApiView.as_view(), name="course-retrieve-update-destroy"),
    path("course/join/<int:course_id>/", CourseJoinApi.as_view(), name="course-join"),
    path("course/personal/", PersonalCoursesListAPIView.as_view(), name="personal-course"),

    path("course_category/", CourseCategoryListCreateApiView.as_view(), name="course-category-list-create"),
    path("course_category/<int:id>/", CourseCategoryRetrieveUpdateDestroyApiView.as_view(),
         name="course-category-retrieve-update-destroy"),

    path("video/", VideoListCreateApiView.as_view(), name="video-list-create"),
    path("video/<int:id>/", VideoRetrieveUpdateDestroyApiView.as_view(), name="video-retrieve-update-destroy"),

    path("blog/", BlogListCreateApiView.as_view(), name="blog-list-create"),
    path("blog/<int:id>/", BlogRetrieveUpdateDestroyApiView.as_view(), name="blog-retrieve-update-destroy"),

    path("comment/", CommentListCreateApiView.as_view(), name="comment-list-create"),
    path("comment/<int:id>/", CommentRetrieveUpdateDestroyApiView.as_view(), name="comment-retrieve-update-destroy"),

    path('ssl-commerz-session/', SSLCommerzSessionAPI.as_view(), name="ssl-commerz-session"),
    path('ipn-verify/', IPNVerifyAPIView.as_view(), name="ipn-verify"),
    path('product-redirect/', ProductRedirectView.as_view(), name="ipn-verify")
]
