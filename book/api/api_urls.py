from django.urls import include,path
from .api_views import *

urlpatterns = [
    #APIs For Book
    path('view/',BookList.as_view()),
    path('create/',BookCreateView.as_view()),
    path('search/',BookSearchView.as_view()),
    #APIs For Chapters
]
