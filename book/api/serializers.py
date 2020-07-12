from rest_framework import generics
from rest_framework import serializers
from book.models import Book,Chapter

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name','isbn13','author']
        optional_fields = ['image']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ChapterSerializer(serializers.Serializer):
    class Meta:
        model = Chapter
        fields = ['name','content','book','author']
        optional_fields = ['next_release',]