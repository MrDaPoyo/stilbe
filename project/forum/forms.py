from django import forms
from django.forms.widgets import HiddenInput
from .models import Thread, Post

class PostCreationForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Reply here.', 'class': 'form-control'}))
    
    class Meta:
        model = Post
        fields = ['content']

class ThreadCreationForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Create a thread.', 'class': 'form-control'}))
    
    class Meta:
        model = Thread
        fields = ['content']
