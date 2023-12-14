from django.urls import path
from .views import UserList, UserDetails, GroupList

app_name = "api"

urlpatterns = [
    path('users/', UserList.as_view(), name="user-list"),
    path('users/<pk>/', UserDetails.as_view(), name="user-detail"),
    path('groups/', GroupList.as_view(), name="group-list"),
]
