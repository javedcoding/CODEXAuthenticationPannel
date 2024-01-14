from django.urls import path
from .views import DataEndpoint

app_name = "api"

urlpatterns = [
    path("user-detail/", DataEndpoint.as_view(), name="user-detail"),
]
