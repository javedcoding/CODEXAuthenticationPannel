from django.urls import path
from .views import DataEndpoint, UserGroups, UserList

app_name = "api"

urlpatterns = [
    path("user-detail/", DataEndpoint.as_view(), name="user-detail"),
    path("user-group/", UserGroups.as_view(), name="user-groups"),
    path("group-users/<int:pk>", UserList.as_view(), name="user-groups"),
]
