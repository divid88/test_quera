from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import RegisterUser, CustomTokenVerifyView, CustomTokenRefreshView, CustomTokenObtainPairView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_verify'),

    path('api/register/', RegisterUser.as_view(), name='register_view'),
]