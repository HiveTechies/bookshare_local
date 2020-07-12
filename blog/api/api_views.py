from rest_framework import generics
from blog.models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

class PostListViews(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    search_fields =('title','author__username')
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class PostRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

