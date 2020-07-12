from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation

from hitcount.models import HitCount, HitCountMixin
from comment.models import Comment
from taggit.managers import TaggableManager
from tinymce import models as tinymce_models

class Post(models.Model, HitCountMixin):
    title = models.CharField(max_length=100)
    content = tinymce_models.HTMLField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = GenericRelation(Comment)
    tags = TaggableManager()
    hit_count_generic = GenericRelation(
    HitCount, object_id_field='object_pk',
    related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
