from django.contrib import admin
from django.urls import path,include
from .views import home_views , doctor_views ,lab_views , pharmacy_views ,blog_views , doctor_detail_view , pharmacy_detail_view

urlpatterns = [
    
    path('',home_views,name="Home"),
    path('doctor/',doctor_views, name="Doctor"),
    path("lab/",lab_views,name="Lab"),
    path('pharmacy/',pharmacy_views,name="Pharmacy"),
    path('blog/',blog_views,name="Blog"),
    path('doctor/k',doctor_detail_view , name="DocDetails"),
    path('pharmacy/p',pharmacy_detail_view,name="PharmacyDetail"),
    

]
