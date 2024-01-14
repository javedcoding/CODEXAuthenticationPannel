from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    The class for database model wiring up
    Contains
    user_name - From registration form (one to one connection with admin)
    first_name -
    last_name -
    phone - From profile update form
    address - From profile update form
    city - From profile update form
    state - From profile update form
    zip - From profile update form
    country - From profile update form
    """

    ROLE_CHOICES = [
        ("Base User", "Base User"),
        ("Admin", "Admin"),
        ("Super Admin", "Super Admin"),
    ]

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Base User")
    provider = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.username} Profile"
