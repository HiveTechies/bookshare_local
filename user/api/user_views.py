from .serializers import *
from rest_framework import generics
#from user.models import Profile
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class UserCreateView(generics.CreateAPIView):
    class Meta:
        serializer_class = UserSerializer
        queryset = User.objects.all()

#class ProfileView(generics.RetrieveUpdateAPIView):
#    class Meta:
#        serializer_class = ProfileSerializer
#        queryset = Profile.objects.all()
#        permission_classes = (IsAuthenticated,)
#        authentication_classes = (TokenAuthentication,)
