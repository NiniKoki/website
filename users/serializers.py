from rest_framework import serializers
from .models import YourUsersModel


class YourUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourUsersModel
        fields = '__all__'
