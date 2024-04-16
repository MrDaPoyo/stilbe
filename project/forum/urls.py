from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('thread/<int:pk>', views.threadView, name='thread'),
    # Add more URL patterns here
]