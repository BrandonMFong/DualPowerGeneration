from django.urls import path, include
from . import views

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("profile/", views.Profile.as_view(), name="profile"),
    path("settings/", views.user_settings.as_view(), name="settings"),


]
