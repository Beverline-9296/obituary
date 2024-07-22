from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_obituary/', views.add_obituary, name='add_obituary'),
]