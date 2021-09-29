from django.urls import path
from .views import (AddressRetrieveUpdateDestroy,
    CurrentUserAddressListDestroyCreate)


urlpatterns = [
    path('', AddressRetrieveUpdateDestroy.as_view()),
    path('current-user/', CurrentUserAddressListDestroyCreate.as_view()),
]