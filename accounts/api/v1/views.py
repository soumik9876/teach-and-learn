from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from accounts.api.v1.serializers import GoogleLoginSerializer, UserSerializer
from accounts.models import Student, Teacher
from core.utils import get_logger, get_debug_str

logger = get_logger()


class AbstractBaseLoginView(GenericAPIView):
    authentication_classes = []

    class Meta:
        abstract = True

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            logger.error(get_debug_str(request, request.user, serializer.errors))
            raise ValidationError(serializer.errors)

        user = serializer.validated_data.get('user')
        created = serializer.validated_data.get('created')

        """ If new user, create student and teacher object for the user """
        if created:
            Student.objects.create(user=user)
            Teacher.objects.create(user=user)

        user_serializer = UserSerializer(instance=user, context={'request': request})
        token, _ = Token.objects.get_or_create(user=user)

        resp = {
            'token': token.key,
            'created': created,
            'user_info': user_serializer.data
        }
        return Response(resp, status=status.HTTP_200_OK)


class GoogleLoginView(AbstractBaseLoginView):
    serializer_class = GoogleLoginSerializer
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
