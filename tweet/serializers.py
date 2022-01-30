from rest_framework import serializers

from .models import User, Tweet


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "created_at")


class TweetSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Tweet
        fields = ("id", "author", "created_at", "author_username")
