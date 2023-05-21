"""
    PROJECT URLS
"""

from django.contrib import admin
from django.urls import path, include
from .views import *
from contest.views import *

urlpatterns = [
    path('',hello_world),
    path('api/category',categoriesAPI),
    path('admin/', admin.site.urls),
]
