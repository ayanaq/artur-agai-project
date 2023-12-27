# users/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model


class CustomUsers(AbstractUser):
    first_name = models.CharField(max_length=50)
    confirmation_code = models.CharField(max_length=20, blank=True)

    # Add related_name to avoid clashes with auth.User.groups
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users_groups')

    # Add related_name to avoid clashes with auth.User.user_permissions
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_users_permissions')

    def __str__(self):
        return self.username

    def generate_confirmation_code(self):
        code = get_random_string(length=20)
        return ConfirmationCode.objects.create(user=self, code=code)

    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

from django.contrib.auth.models import User

class ConfirmationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.code}"

