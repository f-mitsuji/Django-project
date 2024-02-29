from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm, CustomUserLoginForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")


class CustomLoginView(LoginView):
    form_class = CustomUserLoginForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    next_page = reverse_lazy("homepage:home")


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")
