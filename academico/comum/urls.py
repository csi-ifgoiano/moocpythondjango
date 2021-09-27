# -*- coding: utf-8 -*-
from django.urls import path, re_path
from comum.views import home

urlpatterns = [
    path('', home, name='home'),
]
# path('comum/', views.home)