from abc import ABC

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.RelatedField, ABC):
    class Meta:
        model = User

        fields = ["email", "username"]

    def to_representation(self, value):
        return value.email

