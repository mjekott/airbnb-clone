from django.contrib.admin.options import ModelAdmin
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "MALE"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_Korean = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_Korean, "Korean"), (LANGUAGE_ENGLISH, "ENGLISH"))

    CURRENCY_USD = "usd"
    CURRENCY_NG = "ng"
    CURRENCY_CHOICES = ((CURRENCY_NG, "NG"), (CURRENCY_USD, "USD"))

    avatar = models.ImageField(blank=True, upload_to="avatars")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=3, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
