from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator

from .utils import BaseModel


class User(AbstractUser, BaseModel):
    """The implementation of user class with constraints and assumptions."""

    username_validator = UnicodeUsernameValidator()
    # Overriding with respect to same field in AbstractUser
    email = models.EmailField(null=True, blank=True)

    username = models.CharField(
        max_length=10,
        unique=True,
        help_text=(
            'Required. 10 characters and 8 chars atleast. Letters, digits '
            'and @/./+/-/_ only.'
        ),
        validators=[
            username_validator,
            MinLengthValidator(8),
        ],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )


class Tweet(BaseModel):
    """The model that represents individual tweet."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tweets"
    )
    text = models.CharField(max_length=140, validators=[

            MinLengthValidator(2),
        ], )

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Tweets"
        ordering = ("-created_at",)
