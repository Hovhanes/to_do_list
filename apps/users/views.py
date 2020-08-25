from django.contrib.auth.models import User
from rest_framework import viewsets

from apps.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    ordering = ['-pk']
    queryset = User.objects.all().order_by('-pk')
