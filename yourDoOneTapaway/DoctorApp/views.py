from django.shortcuts import render
from AcoountApp.decorators import authenticat_doctor
# Create your views here.

@authenticat_doctor
def doctor_dashboard_views(request):
    params = {
        "title":"Doctor-dashboard"
    }
    return render(request , "doctor/doctorDashboard.html",params)