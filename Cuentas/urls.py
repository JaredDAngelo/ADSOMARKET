from django.urls import path
from . import views

urlpatterns = [
    path('registro', views.registro, name='registro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
]
