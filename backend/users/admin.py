from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserTokens


admin.site.register(User)
admin.site.register(UserTokens)
