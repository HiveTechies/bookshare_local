from django.urls import path,include
from .views import BookCreateView, ChapterDetailView, BookUpdateView, ChapterUpdateView, GenreBookListView, TagBookListView, GenreCreateView
from . import views

urlpatterns = [
    path('all_books/',views.all_books, name="allbooks"),

    # BOOK ROUTES
    path('new/', BookCreateView.as_view(), name="book-create"),
    path('<book_id>/detail', views.book_detail_view, name="detail"),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name="book-update"),
    path('add_favorite/',views.add_favorite, name='favorite'),

    # CHAPTER ROUTES
    path('chapter/<int:pk>/', ChapterDetailView.as_view(), name="chapter-detail"),
    path('chapter/<int:pk>/update/', ChapterUpdateView.as_view(), name="chapter-update"),
    path('newchapter/', views.create_chapter, name="chapter-create"),

    # GENRE ROUTES
    path('genre/new/', GenreCreateView.as_view(), name='create_genre'),
    path('genre/<str:genrename>', GenreBookListView.as_view(), name="genre-book"),
    path('genre/',views.genre, name="genre"),
    path('favorite/',views.favorite, name="favorites"),

    # COLLECTION ROUTES
    path('collection/new/',views.create_collection, name='create_collection'),
    path('collection/', views.collection, name='collection'),
    path('<collection_id>/books_in_collection/', views.books_in_collection, name='books_in_collection'),
    path('add_to_collection/',views.add_book_to_collection, name='add_collection'),
    # EXTERNAL APPS ROUTES
    path('tag/<str:tagname>',TagBookListView.as_view(),name='tag_books'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    #API Views
    path('api/',include('book.api.api_urls',)),
]
