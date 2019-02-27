from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated  
from django.contrib.auth.models import User
from . import serializers


class ListUser(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer