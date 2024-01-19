from django.db import models
from users.models import YourUsersModel


class YourAdminProductsModel(models.Model):
    product_id = models.IntegerField()
    title = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(YourUsersModel, on_delete=models.CASCADE)
