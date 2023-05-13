"""
    PRACTICE SET URLS
"""


from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('getCategoriesAPI',getCategoriesAPI, name="getCategoriesAapi")
]
