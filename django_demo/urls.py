from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django_demo.settings import env, MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
]

if env.str('ENV_TYPE') == 'DEVELOPMENT':
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
