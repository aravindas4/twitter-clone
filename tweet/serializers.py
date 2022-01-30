from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User, Tweet


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user model."""

    class Meta:
        model = User
        fields = ("id", "username", "created_at", "password")
        extra_kwargs = {
            "password": {"write_only": True, "required": True},
        }

    @staticmethod
    def validate_password(data: str) -> str:
        """
        Hash value passed by user.

        :param data: password of a user
        :return: a hashed version of the password
        """
        return make_password(data)


class TweetSerializer(serializers.ModelSerializer):
    """Serializer for Twitter model."""

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
        extra_kwargs = {
            # Because the field is captured while saving the serializer
            "author": {
                "required": False,
            },
        }
