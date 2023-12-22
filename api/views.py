from .serializers import UserProfileSerializer, GroupSerializer
from app.models import UserProfile
from rest_framework import generics, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.contrib.auth.models import Group


# Create the API views
class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ["groups"]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
