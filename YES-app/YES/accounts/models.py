from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, username, display_name=None, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not display_name:
            display_name = username

        user = self.model(  # create an instance in mem
            email=self.normalize_email(email),
            username=username,
            display_name=display_name
        )
        user.set_password(password)  # takes care of encrypting the pass
        user.save()  # save instance to db
        return user

    def create_superuser(self, email, username, display_name, password):
        user = self.create_user(
            email,
            username,
            display_name,
            password
        )
        user.is_staff = True  # so that they can connect to admin
        user.is_superuser = True  # search more about those two
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    display_name = models.CharField(max_length=140)
    date_joined = models.DateTimeField(default=timezone.now)
    # if user wants to delete his account
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # he is not a staff

    objects = UserManager()  # this is an attribute not a field

    # unique identifier in db, what people will login with
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["display_name", "username"]  # search more about this
