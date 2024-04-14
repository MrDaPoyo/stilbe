from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class RegisterForm(UserCreationForm):
    pass

class RegisterView(LoginRequiredMixin, CreateView):
    form_class = RegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    login_url = '/login/'  # Specify the login URL

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()
    
