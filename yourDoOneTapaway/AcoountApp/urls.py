from django.contrib import admin
from django.urls import path,include
from .views import adduser , regDoctor , regLab , regpharmacy ,login_view ,logout_view

urlpatterns = [
    path('signup/',adduser,name="Adduser"),
    path("login/",login_view,name="login"),
    path("logout/",logout_view,name='logout'),
    path('doctorregistration/', regDoctor, name="AddDoctor"),
    path('labregistration/', regLab, name="AddDoctor"),
    path('pharmacyregistration/', regpharmacy, name="AddDoctor"),
]
