from rest_framework import mixins, permissions, status, serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User, Tweet
from .serializers import UserSerializer, TweetSerializer
from .utils import CustomAPIException


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TweetViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # Util classes
    class RecordsSerializer(serializers.Serializer):
        """Ids serializer. Verifies if input data is a list of characters."""

        ids = serializers.ListField(child=serializers.CharField(min_length=1))

    class DateSerializer(serializers.Serializer):
        """Date Serializer. Verifies if input data is date value."""

        date = serializers.DateField()

    def get_queryset(self):
        """Filter tweets of a user."""
        queryset = self.queryset.filter(author=self.request.user)

        if self.action in ["list"]:
            if "date" not in self.request.query_params:
                raise CustomAPIException(
                    message="date query param is required.",
                    status_code=status.HTTP_403_FORBIDDEN,
                )

        # Get the date query parameter
        date_data = self.request.query_params.get("date")

        # Valid if it is a date
        date_serializer = self.DateSerializer(data={"date": date_data})
        date_serializer.is_valid(raise_exception=True)

        # Filter only newer according to the date
        validated_date_data = date_serializer.validated_data["date"]
        queryset = queryset.filter(created_at__date__gte=validated_date_data)

        return queryset

    def perform_create(self, serializer):
        # Saving the author of the tweet
        serializer.save(author=self.request.user)

    @action(methods=["POST"], detail=False, url_path="multi/delete")
    def multi_delete(self, request, *args, **kwargs):
        """Delete multiple tweet records."""

        # Verify ids
        serializer = self.RecordsSerializer(
            data={
                "ids": request.data.get("ids"),
            }
        )
        serializer.is_valid(raise_exception=True)

        # Filter the tweets according to ids and author
        tweet_ids = serializer.validated_data.get("ids")
        queryset = self.queryset.filter(
            id__in=tweet_ids, author=self.request.user
        )

        response = {
            "count": queryset.count(),
            "tweets": self.get_serializer(queryset, many=True).data,
        }

        # delete tweets
        queryset.delete()
        return Response(response)
