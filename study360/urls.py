"""
    PROJECT URLS
"""

from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
]
