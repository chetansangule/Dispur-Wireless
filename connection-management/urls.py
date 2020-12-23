# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:20:46 2020

@author: chetan
"""

from django.urls import path
from . import views

urlpatterns = [
    
    path('services.html',views.services,name='services')
    
    ]