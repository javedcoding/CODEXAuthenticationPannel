from django.urls import path
from oauth2_provider.views import AuthorizationView, TokenView, RevokeTokenView
from .views import DataEndpoint

app_name = "api"

urlpatterns = [
    path("authorize/", AuthorizationView.as_view(), name="authorize"),
    path("token/", TokenView.as_view(), name="token"),
    path("revoke-token/", RevokeTokenView.as_view(), name="revoke-token"),
    path("user-detail/", DataEndpoint.as_view(), name="user"),
]
