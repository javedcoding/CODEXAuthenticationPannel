from typing import Dict
from .serializers import UserProfileSerializer
from django.http import JsonResponse
from oauth2_provider.views.generic import ProtectedResourceView


class DataEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        """
        This method returns the user data of the user.
        """
        data_dict: Dict[str, str] = UserProfileSerializer(request.user).data
        data_dict.pop("password")
        return JsonResponse(data_dict, safe=False)
