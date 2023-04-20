from django.contrib import admin
from django.urls import path,include
from .views import adduser , regDoctor , regLab , regpharmacy

urlpatterns = [
    path('signup/',adduser,name="Adduser"),
    path('doctorregistration/', regDoctor, name="AddDoctor"),
    path('labregistration/', regLab, name="AddDoctor"),
    path('pharmacyregistration/', regpharmacy, name="AddDoctor"),
]
