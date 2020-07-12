from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Book,Chapter,Genre
from django.forms import Textarea
from tinymce.widgets import TinyMCE



class GenreForm(forms.ModelForm):
    class Meta:
        model  = Genre
        fields = '__all__'
    

class DateInput(forms.DateInput):
    input_type = 'date'

class BookForm(forms.ModelForm):
    about = forms.CharField(widget=TinyMCE(attrs={'cols':80,'rows':30}))
    class Meta:
        model  = Book
        fields=['name','about','image','genre','published_date','tags','lang_code','is_explicit','pages']
        widgets = {
            'published_date' : DateInput(),
        }


class ChapterCreateForm(forms.ModelForm):
    book = forms.ModelChoiceField(queryset=Book.objects.none())
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    
    class Meta:
        model = Chapter
        fields = ['name','content','book','next_release']
        widgets = {
            'next_release' : DateInput(), 
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ChapterCreateForm, self).__init__(*args, **kwargs)
        self.fields['book'].queryset=Book.objects.filter(author=user)