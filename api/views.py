from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import OrderingFilter, SearchFilter
from django.contrib.auth.models import User

from . import serializers
from .permissions import UserPermission

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (UserPermission,)
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        return serializers.UserListSerializer if self.action == 'list' else serializers.UserSerializer


class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = User.objects.all()
    serializer_class = serializers.BlogSerializer

    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['username', 'first_name', 'last_name']
    ordering = ['username']
    filter_fields = ['username']