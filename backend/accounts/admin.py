from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserTokens


# admin.site.register(User)
# admin.site.register(UserTokens)


@admin.register(User)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
        "verified",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "phone",
        "date_joined",
        "updated_at",
    ]


@admin.register(UserTokens)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["username", "token", "last_updated"]