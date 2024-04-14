from .views import RegisterView
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from .views import login

urlpatterns = [
    # other urls...
    path('register/', RegisterView.as_view(), name='register'),
    path('', lambda request: redirect('login'), name='home'),
    path('', include("django.contrib.auth.urls")),
    path('logout/', LogoutView.as_view(), name='logout'),
]