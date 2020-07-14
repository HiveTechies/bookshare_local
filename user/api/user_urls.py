from django.urls import path,include
from .user_views import *

urlpatterns = [
#    path('profile/',ProfileView.as_view()),
    path('user_create/',UserCreateView.as_view()),
]
