from django import forms
from .models import Thread, Post

class ThreadCreationForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content']

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        