"""views for the user api."""

from rest_framework import generics,permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import  TokenObtainPairView

from rest_framework.settings import api_settings

from .serializers import (
        UserSerializer,CustomTokenObtainPairSerializer 
    )


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the System"""
    serializer_class = UserSerializer
    
class CreateTokenView(TokenObtainPairView):
    """Create a new token for user"""
    serializer_class=CustomTokenObtainPairSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES    

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    uthentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        """Retrieve and return the authenticated user"""
        return self.request.user