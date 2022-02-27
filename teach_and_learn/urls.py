from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from teach_and_learn.settings import env, MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATIC_URL

api_url_patterns = ([
    path("accounts/v1/", include("accounts.api.v1.urls")),
    path("course/v1/", include("course.api.v1.urls")),
    path("quiz/v1/", include("quiz.api.v1.urls"))
])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns)),
    path('', include('accounts.urls'))
]

if env.str('ENV_TYPE') == 'DEVELOPMENT':
    import debug_toolbar

    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
