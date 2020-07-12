from rest_framework import generics
from .serializers import *
from book.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

class BookView(generics.ListAPIView):
    class Meta:
        serializer_class = BookSerializer
        permission_classes = [IsAuthenticated]
        authentication_classes = [TokenAuthentication]
        def get_queryset(self):
            return Book.objects.all()

class BookList(generics.ListAPIView):
    search_fields = ['name']
    filter_backends = [filters.SearchFilter]
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ChapterView(generics.RetrieveUpdateDestroyAPIView):
    class Meta:
        serializer_class = ChapterSerializer
        queryset = Chapter.objects.all()
        permission_classes = [IsAuthenticated()]
        authentication_classes = [TokenAuthentication()]

class BookGeneric(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'name'
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('name')
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Book.objects.all()


class BookSearchView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ('name','author__username','tags__name')
    

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
