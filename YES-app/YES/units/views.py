from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView  # dont need yet
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class unit_lists(LoginRequiredMixin, ListView):
    model = tempdb  # template should be (model name)_list.html


class unit_detail(LoginRequiredMixin, DetailView):
    model = tempdb
