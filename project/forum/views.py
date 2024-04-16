from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from .models import Thread


# Create your views here.
@login_required
def home(request):
    User = get_user_model()
    users = User.objects.all() 
    return render (request, "forum/home.html", {"users":users})


def threadView(request, pk):
    thread = Thread.objects.get(id=pk)
    title = thread.title
    content = thread.content
    return render(request, "forum/thread.html", {"title": title, "content": content})