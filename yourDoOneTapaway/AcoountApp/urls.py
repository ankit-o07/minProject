from django.contrib import admin
from django.urls import path,include
from .views import adduser , AddDoctor

urlpatterns = [
    path('signup/',adduser,name="Adduser"),
    path('doctorregistration/', AddDoctor, name="AddDoctor")
]
