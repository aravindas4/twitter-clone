from django.db import models
from rest_framework.pagination import PageNumberPagination


def get_short_uuid():
    """Generate Short UUID."""
    return str(uuid.uuid4()).replace("-", "")[:10].upper()


class BaseModel(models.Model):
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
