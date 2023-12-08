from django.db import models
from django.contrib.auth.models import User

# from rest_framework.authtoken.models import Token
from PIL import Image


class UserProfile(models.Model):
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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # token = models.OneToOneField(Token, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(default="profile_images/default.jpg", upload_to="profile_pics")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
