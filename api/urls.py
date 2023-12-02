from django.urls import path
from .views import UserAuthenticationView, UserProfileView

app_name = "api"

urlpatterns = [
    path('authenticate/', UserAuthenticationView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
