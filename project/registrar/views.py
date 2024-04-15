from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied

class RegisterForm(UserCreationForm):
    pass

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')