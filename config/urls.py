from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('addresses.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
