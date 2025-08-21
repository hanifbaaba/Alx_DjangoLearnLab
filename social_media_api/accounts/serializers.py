from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        models = CustomUser
        fields = '__all__'