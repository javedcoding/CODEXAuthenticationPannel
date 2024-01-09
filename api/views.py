from .serializers import UserProfileSerializer
from oauth2_provider.views.generic import ProtectedResourceView


class DataEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return UserProfileSerializer(request.user).data
