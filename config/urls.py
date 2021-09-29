from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Addresses API",
        description="An API for users to manage addresses",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('addresses.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name="redoc"),
]
