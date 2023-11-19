from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils import timezone
from django.db import transaction
from .views import authentication_data


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """

        Creates and saves a User with the given email,and password.
        """

        if not email:
            raise ValueError("The given email must be set")
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)

                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self._create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    class Meta:
        ordering = ("-date_joined",)
        verbose_name = "User Profiles"
        verbose_name_plural = "User Profiles"


class UserTokens(models.Model):
    user = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        on_delete=models.CASCADE,
        verbose_name="user email",
    )
    token = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.access_token = authentication_data["token"]
        self.user = authentication_data["email"]

        super(UserTokens, self).save(*args, **kwargs)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "User Tokens"
        verbose_name_plural = "User Tokens"
