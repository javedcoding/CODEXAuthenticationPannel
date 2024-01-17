from rest_framework import serializers
from app.models import UserProfile
from django.utils import timezone
from rest_framework.authtoken.models import Token

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200, required=True)
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=30, required=False)
    email = serializers.EmailField(max_length=200, required=True)
    password = serializers.CharField(max_length=30,required=True)
    role = serializers.CharField(max_length=30,required=False)
    provider = serializers.CharField(max_length=50,required=False)
    
    class Meta:
        model = UserProfile
        fields = ["username", "first_name", "last_name", "email", "password", "role", "provider"]

    def create(self, validated_data):
        user_instance = UserProfile(**validated_data, registration_datetime=timezone.now())
        user_instance.set_password(validated_data['password'])
        user_instance.save()

        return user_instance

class UserProfileDataSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ["id", "last_login", "is_active", "username", "email", "first_name", "last_name", "role", "provider", "phone", "address", "city", "state", "zip", "country", "registration_datetime"]
        
class UserProfileDataUpdateSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(max_length=200, required=False)
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=30, required=False)
    role = serializers.CharField(max_length=30,required=False)
    provider = serializers.CharField(max_length=50,required=False)
    phone = serializers.CharField(max_length=15, required=False)
    address = serializers.CharField(max_length=255, required=False)
    city = serializers.CharField(max_length=50, required=False)
    state = serializers.CharField(max_length=50, required=False)
    zip = serializers.CharField(max_length=50, required=False)
    country = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "password", "role", "provider", "phone", "address", "city", "state", "zip", "country"]

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.first_name)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.role = validated_data.get('role', instance.role)
        instance.provider = validated_data.get('provider', instance.provider)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.zip = validated_data.get('zip', instance.zip)
        instance.country = validated_data.get('country', instance.country)
        
        password = validated_data.get('password')
        token_message = None
        if password is not None:
            instance.set_password(password)
            # Delete the old token and create a new one
            Token.objects.filter(user=instance).delete()
            Token.objects.create(user=instance)
            token_message = 'Token was not there, so it was created! Please keep it in a safe place!'
        
        instance.save()

        return instance, token_message
    
class UserDeleteSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(required=False)
    token = serializers.CharField(required=False)   