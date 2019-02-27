from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User

from . import serializers
from .permissions import UserPermission


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (UserPermission,)
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        return serializers.UserListSerializer if self.action == 'list' else serializers.UserSerializer