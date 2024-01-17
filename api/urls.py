from django.urls import path
from .views import DataEndpoint, UserProfileDataUpdateView

app_name = "api"

urlpatterns = [
    path("user-detail/", DataEndpoint.as_view(), name="user-detail"),
    path("user-profile-update/", UserProfileDataUpdateView.as_view(), name="user-profile-update"),
]
