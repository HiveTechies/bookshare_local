from book.models import Book
from django.contrib.auth.models import User
from PIL import Image
from django.db import models
from django.urls import reverse


class Collection(models.Model):
    name = models.CharField(max_length=50,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collections")
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class ExplicitReport(models.Model):
    url=models.CharField(max_length=200)
    name_of_book= models.CharField(max_length=100)
    report=models.CharField(max_length=200)

    def __str__(self):
        return f'{name_of_book}'

class Developer(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    languages_known = models.CharField(max_length=100)
    mail= models.CharField(max_length=100)
    contact = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.name}'
