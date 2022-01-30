from django.contrib import admin

from .models import Tweet, User


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
    )
    list_display_links = ("id",)
    search_fields = (
        "id",
        "text",
    )
    list_per_page = 50


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username")
    list_display_links = ("id",)
    search_fields = (
        "id",
        "username",
    )
    list_per_page = 50
