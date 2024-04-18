from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from .models import Thread
from .forms import PostCreationForm, ThreadCreationForm, PostDeletionForm
from django.contrib import messages
import time


# Create your views here.
@login_required
def home(request):
    User = get_user_model()
    users = User.objects.all() 
    return render(request, "forum/home.html", {"threads":Thread.objects.all()})

@login_required
def threadView(request, pk):
    user = request.user
    thread = Thread.objects.get(id=pk)
    poster = thread.user
    title = thread.title
    content = thread.content
    created_at = thread.created_at
    posts = thread.post_set.all()
    form = PostCreationForm()

    context = {
        "title": title,
        "content": content,
        "user": user,
        "posts": posts,
        "form": form,
        "created_at": created_at,
        "poster": poster
    }

    if request.method == "POST":
        form = PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.thread = thread
            post.save()
            messages.success(request, "Post created successfully!")
            return render(request, "forum/thread.html", context)
    return render(request, "forum/thread.html", context)

@login_required
def redirectHome(request):
    return redirect("home")

@login_required
def userList(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, "forum/profile_list.html", {"users":users})

@login_required
def createThread(request):
    User = get_user_model()
    form = ThreadCreationForm()
    if request.method == "POST":
        form = ThreadCreationForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.user = request.user
            thread.title = form.cleaned_data["title"]
            thread.content = form.cleaned_data["content"]
            thread.save()
            messages.success(request, "Thread created successfully!")
            time.sleep(5)
            return redirect("/thread/"+str(thread.id))
    return render(request, "forum/create_thread.html", {"form":form})

@login_required
def deletePost(request):
    form = PostDeletionForm()
    if form.is_valid():
        post = form.save(commit=False)
        post.id = form.cleaned_data["id"]
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect("home")
    else:
        pass