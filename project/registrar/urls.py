from .views import RegisterView
from django.urls import path, include

urlpatterns = [
    # other urls...
    path('register/', RegisterView.as_view(), name='register'),
    path('', include("django.contrib.auth.urls")),
]