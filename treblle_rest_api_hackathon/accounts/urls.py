from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .serializers import CustomTokenObtainPairSerializer

from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("create/", views.CreateUserView.as_view(), name="create"),
    path('token/', views.CreateTokenView.as_view(serializer_class=CustomTokenObtainPairSerializer), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("me/", views.ManageUserView.as_view(), name="me"),    
]