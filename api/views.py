from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import UserRegisterSerializer, UserAndUserProfileSerializer, UserProfileUpdateSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from app.models import UserProfile

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            # Generate a token for the newly registered user
            token, _ = Token.objects.get_or_create(user=user)

            # Include the token in the response
            response_data = {
                'message': 'User registered successfully!!',
                'username': user.username,
                'email': user.email,
                'token': token.key 
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginAndDataView(APIView):
    def post(self, request):
        username_or_email = request.data.get('username_or_email')
        password = request.data.get('password')
        token_key = request.data.get('token')

        if token_key:
            # Token verification
            try:
                token = Token.objects.get(key=token_key)
                user = token.user
            except Token.DoesNotExist:
                return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
        elif username_or_email and password:
            # Username/email and password authentication
            user = authenticate(username=username_or_email, password=password)
            if user is None:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Invalid request. Provide username/email and password or token.'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate a token for the authenticated user (if not provided in the request)
        if not token_key:
            token, _ = Token.objects.get_or_create(user=user)

        # Use the UserAndUserProfileSerializer for the response
        serializer = UserAndUserProfileSerializer(user)

        # Include user details and profile details in the response, without the token
        response_data = {
            'message': 'Login successful. User data retrieved successfully!!',
            'user': serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)
    
class UserProfileDataUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
        serializer = UserProfileUpdateSerializer(user_profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Profile updated successfully!!!'
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class UserDeleteTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get_user_token(self, user):
        try:
            return Token.objects.get(user=user)
        except Token.DoesNotExist:
            return None

    def delete_user_token(self, user):
        token = self.get_user_token(user)
        if token:
            token.delete()

    def post(self, request):
        user = request.user
        self.delete_user_token(user)
        return Response({'message': 'Logout successful. Token deleted successfully!!'}, status=status.HTTP_200_OK)
