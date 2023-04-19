from django.contrib import admin
from django.urls import path,include
from .views import pharmacy_dashboard_views

urlpatterns = [
    
    path('dashboard/',pharmacy_dashboard_views,name="Dashboard_pharma"),
    
    

]
