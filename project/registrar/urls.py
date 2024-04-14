from .views import RegisterView, logout_view
from django.urls import path, include

urlpatterns = [
    # other urls...
    path('register/', RegisterView.as_view(), name='register'),
    path('', include("django.contrib.auth.urls")),
    path('logout/', logout_view, name='logout')
]