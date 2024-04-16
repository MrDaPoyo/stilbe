from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('thread/<int:pk>', views.threadView, name='thread'),
    path('', views.redirectHome, name='redirect-home'),
    # Add more URL patterns here
]