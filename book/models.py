from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from datetime import date,timedelta
from django.core.files.storage import FileSystemStorage
from .validators import validate_file_extension
from taggit.managers import TaggableManager
from languages.fields import LanguageField
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from hitcount.models import HitCount
from hitcount.models import HitCountMixin
from star_ratings.models import Rating
from tinymce import models as tinymce_models
class Genre(models.Model):
    genre = models.CharField(max_length=30)
    image = models.CharField(max_length=1000,default='https://www.southlakessentinel.com/wp-content/uploads/2019/03/book-article-pic.jpg')

    def __str__(self):
        return self.genre

    def get_absolute_url(self):
        return reverse('allbooks')


class Book(models.Model, HitCountMixin):
    name = models.CharField(max_length=200)
    about = tinymce_models.HTMLField()
    AUTHOR_STATUS = (("D", "Draft"), ("P", "Published"))
    author_status=models.CharField(max_length=2, choices=AUTHOR_STATUS)
    image = models.CharField(max_length=1000,default='https://drive.google.com/file/d/1l3wxpy7k4hrXm_l1T94ENv0dMFa9KeS7/view?usp=sharing')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    BOOK_STATUS=(('C','Completed'), ('O','On Going'))
    book_status=models.CharField(max_length=2, choices=BOOK_STATUS)
    pages = models.PositiveIntegerField(default=0)
    favorite = models.ManyToManyField(User, related_name="favorite")
    genre = models.ManyToManyField(Genre, related_name="book_genre")
    isbn13 = models.CharField(max_length=20)
    published_date = models.DateField(default=timezone.now)
    published_year = models.CharField(max_length=4)
    publisher = models.CharField(max_length=60)
    tags = TaggableManager()
    lang_code = LanguageField(max_length=8)
    is_explicit = models.BooleanField(default=False)
    comments = GenericRelation(Comment)
    ratings = GenericRelation(Rating, related_query_name='book_rating')
    hit_count_generic = GenericRelation(
    HitCount, object_id_field='object_pk',
    related_query_name='hit_count_generic_relation')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save()


class Chapter(models.Model):
    name = models.CharField(max_length=40)
    content = tinymce_models.HTMLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="chapters")
    published_date = models.DateField(default=timezone.now)
    next_release = models.DateField(unique=False,default = timezone.now()+timedelta(days=7))
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("chapter-detail", args=[str(self.id)])
