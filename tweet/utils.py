import uuid

from django.db import models
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.pagination import PageNumberPagination


def get_short_uuid():
    """Generate Short UUID."""
    return str(uuid.uuid4()).replace("-", "")[:10].upper()


class BaseModel(models.Model):
    """Abstract model for all the concrete models."""

    id = models.CharField(
        max_length=12, default=get_short_uuid, editable=False, primary_key=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomPageNumberPagination(PageNumberPagination):
    """Custom Pagination Class."""

    page_size = 50
    page_size_query_param = "limit"
    max_page_size = 1000


class CustomAPIException(APIException):
    """
    Custom API Exception class. Can be customized for status code and error
    details. For usage at Serializer validations.
    """

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "A server error occurred."
    field = "detail"

    def __init__(self, message=None, field=None, status_code=None):  # noqa
        if status_code:
            self.status_code = status_code
        if message:
            self.message = message
        if field:
            self.field = field

        self.detail = {self.field: self.message}
