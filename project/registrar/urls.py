from .views import RegisterView
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # other urls...
    path('', include("captcha.urls")),
    path('', include(("django.contrib.auth.urls", "auth"))),  
    path('register/', RegisterView.as_view(redirect_authenticated_user=True), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("login/", auth_views.LoginView.as_view(redirect_authenticated_user=True)),
]
