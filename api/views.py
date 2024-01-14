from typing import Dict

from rest_framework import generics
from app.models import UserProfile
from .serializers import UserProfileSerializer, GroupSerializer
from django.http import JsonResponse
from django.contrib.auth.models import Group
from oauth2_provider.views.generic import ProtectedResourceView


class DataEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        """
        This method returns the user data of the user.
        """
        data_dict: Dict[str, str] = UserProfileSerializer(request.user).data
        data_dict.pop("password")
        return JsonResponse(data_dict, safe=False)


class UserGroups(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        """
        This method returns the groups of the user. If the user is a superuser, it returns all the groups. Otherwise,
        it returns the groups the user is part of.
        """
        user = UserProfileSerializer(request.user)

        if user["is_superuser"]:
            queryset = Group.objects.all()
        else:
            queryset = Group.objects.filter(name__in=user["groups"])

        print(queryset)
        return JsonResponse(GroupSerializer(queryset, many=True).data, safe=False)


class UserList(ProtectedResourceView, generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        """
        This method returns the users of the group. The group name is passed as a parameter in the URL.
        """
        group_id = self.kwargs["pk"]
        return JsonResponse(UserProfile.objects.filter(groups__id=group_id), safe=False)
