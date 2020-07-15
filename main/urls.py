from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar



urlpatterns = [
    path('', include('user.urls')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),
    path('book/', include('book.urls')),
    path('comment/', include('comment.urls')),
    path('terms/', include('termsandconditions.urls')),
    path('maintenance-mode/', include('maintenance_mode.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path("account/", include("account.urls")),
    path("teams/", include("pinax.teams.urls", namespace="pinax_teams")),
    path('tinymce/', include('tinymce.urls')),
    path('auth/',include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path("blog/", include("blog.urls")),
    path('tracking/', include('tracking.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
    path('todo/', include('todo.urls', namespace="todo")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'user.views.error_404_view'
handler500 = 'user.views.error_500_view'
