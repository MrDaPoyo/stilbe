from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied

class AnonymousRequiredMixin(AccessMixin):
    """Verify that the current user is not authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect("home")

class RegisterForm(UserCreationForm):
    pass

class RegisterView(AnonymousRequiredMixin, CreateView):
    form_class = RegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    login_url = '/login/'  # Specify the login URL
    login_url = '/login/'  # Specify the login URL

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()
    
