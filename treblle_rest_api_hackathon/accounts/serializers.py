"""
Serializer for the user Api views.
"""
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
#from django.utils.translation import ugettext_lazy as _
from rest_framework.authentication import authenticate
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""
    
    class Meta:
        model =get_user_model()
        fields = ["email","password","name"]
        extra_kwargs = {"password":{"write_only":True, "min_length":5}}
        
    def create(self,validated_data):
        """creates and returns a user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self,instance,validated_data):
        """Update and return User"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        
        if password:
            user.set_password(password)
            user.save()
            
        return user
class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style = {"input_type":"password"}
    )
    
    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get("email")
        password = attrs.get("password")
        user =  authenticate(
            request=self.context.get("request"),
            username = email,
            password =password,
            )
        if not user:
            msg = ("Unable to authenticate with the provided details")
            raise serializers.ValidationError(msg,code="authorization") 
        attrs['user'] = user

        return attrs
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.name
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.name
        data['email'] = self.user.email
        

        return data
