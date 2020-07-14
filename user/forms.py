from django import forms
from .models import Profile, Developer, ExplicitReport


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'quote', 'aboutme']

class ReportForm(forms.ModelForm):
    url = forms.URLField()
    name_of_book= forms.CharField(widget=forms.TextInput(attrs={'size':15, 'maxlength':40}))
    report = forms.CharField(widget=forms.TextInput(attrs={'size':15, 'max_length':60}))

    class Meta:
        model = ExplicitReport
        fields = ['url','name_of_book','report']


class DeveloperRegistrationForm(forms.ModelForm):
    mail = forms.EmailField(widget=forms.TextInput(attrs={'size':15, 'maxlength':50}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'size':15, 'maxlength':20}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'size':15, 'maxlength':20}))
    languages_known = forms.CharField(widget=forms.TextInput(attrs={'size':15, 'max_length':60}))

    class Meta:
        model = Developer
        fields = ['name', 'first_name', 'last_name', 'about', 'mail', 'languages_known', 'contact']


