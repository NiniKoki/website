from rest_framework import serializers
from .models import YourEmailVerificationModel


class YourEmailVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourEmailVerificationModel
        fields = '__all__'
