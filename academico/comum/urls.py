# -*- coding: utf-8 -*-
from django.urls import path
from .views import cadastro, login, logout, home, edit_perfil, ver_perfil

urlpatterns = [
    path('', home, name='home'),
    path('cadastro', cadastro, name='cadastro'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('editar_perfil', edit_perfil, name='editar_perfil'),
    path('ver_perfil', ver_perfil, name='ver_perfil'),
]
