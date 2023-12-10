from django.urls import path
from .views import UserList, UserDetails, GroupList
from rest_framework.authtoken.views import obtain_auth_token

app_name = "api"

urlpatterns = [
    # path("authenticate/", UserAuthenticationView.as_view(), name="user-login"),
    # path("profile/", UserProfileView.as_view(), name="user-profile"),
    path('token/', obtain_auth_token, name='token_obtain_pair'),
    path('users/', UserList.as_view(), name="user-list"),
    path('users/<pk>/', UserDetails.as_view(), name="user-detail"),
    path('groups/', GroupList.as_view(), name="group-list"),
]
