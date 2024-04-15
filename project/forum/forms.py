from django import forms
from .models import Thread, Post

class ThreadCreationForm(forms.ModelForm):
    class Meta:
        model = Thread
        content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Write your initial post here...', 'class': 'form-control'}))
        fields = ['title', 'content']

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        