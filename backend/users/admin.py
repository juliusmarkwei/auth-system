from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserTokens


# admin.site.register(User)
# admin.site.register(UserTokens)


@admin.register(User)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "telephone",
        "date_joined",
    ]


@admin.register(UserTokens)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["email", "token", "last_updated"]
