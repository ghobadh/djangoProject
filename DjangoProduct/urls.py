"""
Name: urls.py
Author: Gavin Hashemi
Date: 2024-09-26 11:44 a.m.
Description:

"""

from django.urls import path
from  . import views


urlpatterns=[
    path('', views.index),
    path('new', views.new)
]