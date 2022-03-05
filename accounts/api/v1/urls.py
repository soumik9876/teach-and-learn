from importlib import import_module

from django.urls import path

from accounts.api.v1.views import GoogleLoginView, StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView, \
    TeacherListCreateAPIView, TeacherRetrieveUpdateDestroyAPIView

try:
    from allauth.socialaccount import providers
except ImportError:
    raise ImportError("allauth needs to be added to INSTALLED_APPS.")

app_name = 'account-api-v1'
urlpatterns = [
    path('login/google/', GoogleLoginView.as_view(), name="google-login"),
    path('student/', StudentListCreateAPIView.as_view(), name="student-list-create"),
    path('student/<int:id>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name="student-retrieve-update-destroy"),
    path('teacher/', TeacherListCreateAPIView.as_view(), name="teacher-list-create"),
    path('teacher/<int:id>/', TeacherRetrieveUpdateDestroyAPIView.as_view(), name="teacher-retrieve-update-destroy"),
]
