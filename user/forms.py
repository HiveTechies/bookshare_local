from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Developer


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'size':15, 'maxlength':50}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'size':30, 'maxlength':50}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'size':20, 'maxlength':20}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'size':20, 'maxlength':20}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'quote', 'country', 'aboutme']

class DeveloperRegistrationForm(forms.ModelForm):
    mail = forms.EmailField(widget=forms.TextInput(attrs={'size':15, 'maxlength':50}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'size':15, 'maxlength':20}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'size':15, 'maxlength':20}))
    languages_known = forms.CharField(widget=forms.TextInput(attrs={'size':15, 'max_length':60}))

    class Meta:
        model = Developer
        fields = ['name', 'first_name', 'last_name', 'about', 'mail', 'languages_known', 'contact']


