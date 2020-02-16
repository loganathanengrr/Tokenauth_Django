from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, views, response

from .serializers import UserSerializer

User = get_user_model()

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticated, )
