from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class CustomLoginView(LoginView):
    form_class = CustomUserLoginForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('paper_list')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
