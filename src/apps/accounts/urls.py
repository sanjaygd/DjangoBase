from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import ( 
    RegisterUserView,
    UserListView
)

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='user-registration'),
    path('users/', UserListView.as_view(), name='user-list'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]