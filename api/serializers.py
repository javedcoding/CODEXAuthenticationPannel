from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from django.contrib.auth.models import User
from app.models import UserProfile

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["image", "first_name", "last_name", "phone", "address", "city", "state", "zip", "country"]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["image", "first_name", "last_name", "phone", "address", "city", "state", "zip", "country"]

class UserAndUserProfileSerializer(WritableNestedModelSerializer):
    profile = UserProfileSerializer(source='userprofile')  # Use the correct related name

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "profile"]

class UserRegisterSerializer(WritableNestedModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = UserProfileUpdateSerializer(required=False)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password", "profile"]

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        password = validated_data.pop('password', None)

        user_instance = User(**validated_data)
        if password is not None:
            user_instance.set_password(password)
        user_instance.save()

        if profile_data:
            UserProfile.objects.create(user=user_instance, **profile_data)

        return user_instance
        
class UserProfileDataUpdateSerializer(WritableNestedModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "profile"]

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        if profile_data:
            profile = instance.userprofile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()

        return instance