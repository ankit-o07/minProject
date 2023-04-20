from django.contrib import admin
from django.urls import path,include
from .views import adduser

urlpatterns = [
    path('signup/',adduser,name="Adduser")
]
