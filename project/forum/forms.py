from django import forms
from django.forms.widgets import HiddenInput
from django.contrib.auth import User
from .models import Thread, Post

class PostCreationForm(forms.ModelForm):
    user = forms.CharField(required=True, widget=HiddenInput())
    thread = forms.CharField(required=True, widget=HiddenInput())
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Write your initial post here...', 'class': 'form-control'}))
    
    class Meta:
        model = Post
        fields = ['thread', 'content']

        