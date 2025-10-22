from django.urls import path
from UserSetUp.users.views.serializer_view import createUser


urlpatterns = [
    path('createUser/', createUser, name='createUser' ),
]