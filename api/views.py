from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from .serializers import UserProfileSerializer
from app.models import UserProfile


class UserAuthenticationView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        # username and password are required for authentication
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            # if the user is successfully authenticated return it's token
            return Response({"token": user.auth_token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve the authenticated user
        authenticated_user = request.user

        user_profile = UserProfile.objects.get(user=authenticated_user)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
