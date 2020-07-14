from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.contrib import messages


urlpatterns = [
    path('',views.home, name='home'),
    path('trending/', views.trending,name="trending"),
    path('profile/', views.profile, name='profile'),
    path('view_profile/<str:username>', views.view_profile, name='profile_detail'),
    path('studio/',views.studio,name='studio'),
    path('following/',views.following,name='following'),
    path('messages/', include('postman.urls', namespace='postman'), name='messages'),
    path('user_search/', views.user_search, name='user_search'),
    path('report/',views.report, name='report'),
    path('report_thanks/', views.report_thanks, name='report_thanks'),
    #  friendship app
    path('follow/',views.add_or_remove_follow),
    path('friendship/', include('friendship.urls')),
    path('tellme/', include("tellme.urls")),
    #user api
    path('api/',include('user.api.user_urls')),
    #Developers routes

    path('dev_home/',views.dev_home, name='dev_home'),
#    path('dev_form/',views.dev_form),
    path('dev_thanks/',views.dev_thanks, name='dev_thanks'),
#OPEN SOURCE URLS
    path('opensource/',views.opensource, name='opensource')
]

