from django.urls import include, path
from rest_framework import routers

from .views import (
    UserViewSet, TweetViewSet
)

app_name = "tweets"
router = routers.SimpleRouter()

router.register(r"user", UserViewSet, basename="user")
router.register(r"tweet", TweetViewSet, basename="tweet")

urlpatterns = [
    path("", include(router.urls)),
]
