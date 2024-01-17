from django.urls import path
from .views import UserRegisterView, UserLoginAndDataView, UserProfileDataUpdateView, UserDeleteTokenView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginAndDataView.as_view(), name='user-login'),
    path('update-profile/', UserProfileDataUpdateView.as_view(), name='update-profile'),
    path('delete/', UserDeleteTokenView.as_view(), name='delete'),
]