from .views import RegisterView, LoginView
from django.urls import path

urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view())
]
