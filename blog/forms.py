from tinymce.widgets import TinyMCE
from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.forms import Textarea

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols':80,'rows':30}))
    class Meta:
        model = Post
        fields = ['title','content','tags']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)
    
