from django.contrib import admin
from django.urls import path,include
from .views import doctor_dashboard_views

urlpatterns = [
   path('dashboard/',doctor_dashboard_views,name="DoctorDashboard")

]
