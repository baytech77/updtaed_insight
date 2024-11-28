from django.shortcuts import render
from user_app.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ChangePasswordView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/password_change_form.html'