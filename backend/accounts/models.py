from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils import timezone
from django.db import transaction


class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, password, phone, **other_fields):
        if not email:
            raise ValueError(_("You must provide an email address"))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, first_name, last_name, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")

        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")

        return self.create_user(username, first_name, last_name, email, password, **other_fields)



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=40, unique=True)
    is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone", "first_name", "last_name"]

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
    
    def __str__(self):
        return self.username

    class Meta:
        ordering = ("-date_joined",)
        verbose_name = "User"
        verbose_name_plural = "Users"


class EmailConfirmationToken(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Email Confirmation Token"
        verbose_name_plural = "Email Confirmation Tokens"

