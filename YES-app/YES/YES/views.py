from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView  # dont need yet

# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"


class AboutView(TemplateView):
    template_name = "about.html"


class LogInView(TemplateView):
    template_name = "login.html"
