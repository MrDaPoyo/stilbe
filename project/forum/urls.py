from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.redirectHome, name='redirect-home'),
    path('thread/<int:pk>', views.threadView, name='thread'),
    path('user_list', views.userList, name='profile-list'),
    path('create_thread', views.createThread, name='create-thread'),
# Add more URL patterns here
]