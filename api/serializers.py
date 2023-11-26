from app.models import Profile
from rest_framework import serializers


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['__all__']
