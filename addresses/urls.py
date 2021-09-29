from django.urls import path
from .views import (AddressRetrieveUpdateDestroy,
    AddressListDestroyCreateCurrentUser)


urlpatterns = [
    path('', AddressRetrieveUpdateDestroy.as_view()),
    path('current-user/', AddressListDestroyCreateCurrentUser.as_view()),
]