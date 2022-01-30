from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User, Tweet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "created_at", "password")
        extra_kwargs = {
            "password": {"write_only": True, "required": True},
        }

    @staticmethod
    def validate_password(value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)


class TweetSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Tweet
        fields = (
            "id",
            "author",
            "created_at",
            "author_username",
            "text",
        )
