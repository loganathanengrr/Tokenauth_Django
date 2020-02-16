from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token as create_token
from .views import CreateUserView, UserListView

urlpatterns = [
    path('create_user', CreateUserView.as_view(), name='create_user'),
    path('users', UserListView.as_view(), name='user_list'),
    path('create_token', create_token, name='create_token'),
]