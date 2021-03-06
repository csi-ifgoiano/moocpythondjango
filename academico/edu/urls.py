# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/<int:pk>/', views.cursos_detail, name='cursos_detail'),
    path('efetuar_matricula/', views.efetuar_matricula, name='efetuar_matricula'),
    path('comprovante_matricula/', views.comprovante_matricula, name='comprovante_matricula'),
]