from django.contrib import admin
from .models import Thread, Post
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Thread)
admin.site.register(Post)