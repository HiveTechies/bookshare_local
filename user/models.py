from book.models import Book
from django.contrib.auth.models import User
from PIL import Image
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField


class Collection(models.Model):
    name = models.CharField(max_length=50,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collections")
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="user.png", upload_to="profile_pics")
    country = CountryField(blank_label='(select country)')
    quote = models.CharField(max_length=80, default="n")
    aboutme = models.TextField(max_length=150, default="n")
    is_author = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('profile')