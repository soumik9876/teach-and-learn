from importlib import import_module

from django.urls import path

from accounts.api.v1.views import GoogleLoginView

try:
    from allauth.socialaccount import providers
except ImportError:
    raise ImportError("allauth needs to be added to INSTALLED_APPS.")

app_name = 'account-api-v1'
urlpatterns = [
    path('login/google/', GoogleLoginView.as_view(), name="google-login")
]
