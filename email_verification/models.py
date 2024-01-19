from django.db import models
from users.models import YourUsersModel


class YourEmailVerificationModel(models.Model):
    user = models.ForeignKey(YourUsersModel, on_delete=models.CASCADE)
    email = models.EmailField()
    verification_token = models.CharField(max_length=100)
