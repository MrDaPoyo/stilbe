from django import forms
from .models import Thread, Post

class ThreadCreationForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Write your initial post here...', 'class': 'form-control'}))
    
    class Meta:
        model = Thread
        fields = ['title', 'content']

        