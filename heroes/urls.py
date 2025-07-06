from django.urls import path
from . import views
from django.contrib.auth.views import LoginView#,LogoutView
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name='home'),
    path("add/", views.add_hero, name='add_hero'),
    path("heroes/", views.hero_list, name="hero_list"),
    path("hero/<int:id>/", views.hero_detail, name="hero_detail"),
    path("delete/<int:id>/", views.delete_hero, name="delete_hero"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name='login'),
    path("logout/", views.logout_view, name="logout")
]