from rest_framework import serializers
from .models import YourAdminProductsModel


class YourAdminProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourAdminProductsModel
        fields = '__all__'
