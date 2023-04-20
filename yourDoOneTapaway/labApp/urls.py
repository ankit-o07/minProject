from django.contrib import admin
from django.urls import path,include
from .views import lab_dashboard_views

urlpatterns = [
    
    path('dashboard/',lab_dashboard_views,name="Dashboard_lab"),
    
    

]
