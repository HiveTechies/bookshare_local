from django.urls import path,include

from .views import (
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    TagPostListView,
    UserPostListView,
    post_create,
)
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', post_create, name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('tag/<str:tagname>',TagPostListView.as_view(),name='tag_posts'),
    path('api/',include('blog.api.api_urls')),
]