from django.db import models


class YourUsersModel(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100)
