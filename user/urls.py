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
    path('about/',views.about,name="about"),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user_login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user_logout'),
    path('messages/', include('postman.urls', namespace='postman'), name='messages'),
    path('user_search/', views.user_search, name='user_search'),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(
             template_name='user/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='user/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='user/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='user/password_reset_complete.html'
         ),
         name='password_reset_complete'),
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

