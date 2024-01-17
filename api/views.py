import json
from typing import Dict
from rest_framework import status
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserProfileSerializer, UserProfileUpdateSerializer

from oauth2_provider.views.generic import ProtectedResourceView


class DataEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        """
        This method returns the user data of the user.
        """
        data_dict: Dict[str, str] = UserProfileSerializer(request.user).data
        data_dict.pop("password")
        data_dict.pop("is_superuser")
        data_dict.pop("user_permissions")
        return JsonResponse(data_dict, safe=False)

    def post(self, request, *args, **kwargs):
        return JsonResponse({"message": "POST method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@method_decorator(csrf_exempt, name="dispatch")
class UserProfileDataUpdateView(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"message": "GET method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, *args, **kwargs):
        """
        This method updates the user profile data of the user.
        """
        data = json.loads(request.body.decode("utf-8"))

        serializer = UserProfileUpdateSerializer(request.user, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse({"message": "Profile updated successfully!!!"}, status=status.HTTP_200_OK)
