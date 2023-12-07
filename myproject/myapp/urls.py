# myapp/urls.py
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('home/', home, name='home'),
    path('index/', index, name='index'),
    path('salir/', salir, name='salir'),
]




