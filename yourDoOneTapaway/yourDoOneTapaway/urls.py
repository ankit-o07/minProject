from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("patientApp.urls")),
    path('pharmacy/',include("pharmaApp.urls")),
    path('lab/',include("labApp.urls")),
    path('account/',include("AcoountApp.urls")),
    path('doctor/',include("DoctorApp.urls"))
]
