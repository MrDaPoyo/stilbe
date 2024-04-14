from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
# Create your views here.
@login_required
def home(request):
    return render(request, 'forum/home.html')