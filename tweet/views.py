from rest_framework import mixins, viewsets
from .models import User, Tweet
from .serializers import UserSerializer, TweetSerializer


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TweetViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
