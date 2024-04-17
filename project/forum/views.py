from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from .models import Thread
from.forms import PostCreationForm, ThreadCreationForm
from django.contrib import messages


# Create your views here.
@login_required
def home(request):
    User = get_user_model()
    users = User.objects.all() 
    return render (request, "forum/home.html", {"threads":Thread.objects.all()})

@login_required
def threadView(request, pk):
    user = request.user
    thread = Thread.objects.get(id=pk)
    poster = thread.user
    title = thread.title
    content = thread.content
    posts = thread.post_set.all()
    form = PostCreationForm()
    if request.method == "POST":
        form = PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.thread = thread
            post.save()
            messages.success(request, "Post created successfully!")
            return render(request, "forum/thread.html", {"title": title, "content": content, "user": user, "posts":posts, "form":form})
    return render(request, "forum/thread.html", {"title": title, "content": content, "user": user, "posts":posts, "poster":poster, "form":form})

@login_required
def redirectHome(request):
    return redirect("home")

@login_required
def userList(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, "forum/profile_list.html", {"users":users})

@login_required
def userList(request):
    User = get_user_model()
    form = ThreadCreationForm()
    return render(request, "forum/create_thread.html", {"form":form})