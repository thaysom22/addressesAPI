from django.urls import path
from .views import (AddressRetrieveUpdateDestroy,
    CurrentUserAddressListDestroyCreate)


urlpatterns = [
    path('<int:pk>/', AddressRetrieveUpdateDestroy.as_view()),
    path('current-user/', CurrentUserAddressListDestroyCreate.as_view()),
]