from django.contrib import admin
from django.urls import path,include
from .views import home_views , doctor_views ,lab_views , pharmacy_views ,blog_views , doctor_detail_view , pharmacy_detail_view

urlpatterns = [
    
    path('',home_views,name="Home"),
    
    

]
