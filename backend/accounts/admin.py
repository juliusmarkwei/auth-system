from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, EmailConfirmationToken


@admin.register(User)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
        "is_verified",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "phone",
        "date_joined",
        "updated_at",
    ]


@admin.register(EmailConfirmationToken)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at", "updated_at"]
    