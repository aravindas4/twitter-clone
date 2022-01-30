from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserViewSet, TweetViewSet

app_name = "tweets"
router = routers.SimpleRouter()

router.register(r"user", UserViewSet, basename="user")
router.register(r"tweet", TweetViewSet, basename="tweet")

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
