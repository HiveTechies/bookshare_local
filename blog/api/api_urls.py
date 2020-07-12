from django.urls import path,include
from . import api_views as views

urlpatterns = [
    path('view_posts/<int:pk>',views.PostRetrieveView.as_view()), 
    path('search_posts/',views.PostListViews.as_view()), 
    path('create_post/',views.PostCreateView.as_view())
]