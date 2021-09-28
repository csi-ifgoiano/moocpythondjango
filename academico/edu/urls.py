# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cursos/', views.listar_cursos, name='listar_cursos'),
]
#path('', home, name='home'),
# path('comum/', views.home)