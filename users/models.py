from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from common.models import BaseModel


class UserManager(BUM):
    def create_user(
        self,
        username,
        email,
        is_active=True,
        is_admin=False,
        password=None,
    ):
        if not username:
            raise ValueError("user must have username")
        if not email:
            raise ValueError("user must have email")

        email = self.normalize_email(email.lower())

        user = self.model(
            username=username,
            email=email,
            is_active=is_active,
            is_admin=is_admin,
        )
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            is_active=True,
            is_admin=True,
        )

        user.is_superuser = True

        user.save(using=self._db)
        return user


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        max_length=100,
        unique=True,
        validators=[username_validator],
    )
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self) -> str:
        return self.username

    @property
    def is_staff(self):
        return self.is_admin
