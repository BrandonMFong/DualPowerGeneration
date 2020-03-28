from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from .models import User


# Create your views here.
from . import forms


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = '../login'
    template_name = "accounts/signup.html"


class Profile(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


class user_settings(LoginRequiredMixin, TemplateView):
    template_name = "accounts/account_settings.html"
