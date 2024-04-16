from django import forms
from django.forms.widgets import HiddenInput
from .models import Thread, Post

class PostCreationForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Write your initial post here...', 'class': 'form-control'}))
    
    class Meta:
        model = Post
        fields = ['content']

        