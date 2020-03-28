from django.urls import path
from .views import *

urlpatterns = [
    path('', unit_lists.as_view(), name='unit-list'),
    path('<int:pk>', unit_detail.as_view(), name='unit-detail'),
]
