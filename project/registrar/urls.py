from .views import RegisterView
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # other urls...
    path('register/', RegisterView.as_view(), name='register'),
    path('', lambda request: redirect('login'), name='home'),
    path('', include("django.contrib.auth.urls")),
]