from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from .forms import RegisterForm

class RegisterView(AccessMixin, CreateView):
        form_class = RegisterForm
        template_name = 'signup.html'
        redirect_authenticated_user = True
        success_url = reverse_lazy('auth:login')
        redirect_field_name = 'forum:home'

        def dispatch(self, request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect('home')
            return super().dispatch(request, *args, **kwargs)