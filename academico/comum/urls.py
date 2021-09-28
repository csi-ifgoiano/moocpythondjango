# -*- coding: utf-8 -*-
from django.urls import path
from .views import cadastro, login, logout, index



urlpatterns = [
    path('', index, name='index'),
    path('cadastro', cadastro, name='cadastro'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]
