from django.shortcuts import render

# Create your views here.

def doctor_dashboard_views(request):
    params = {
        "title":"Doctor-dashboard"
    }
    return render(request , "doctor/doctorDashboard.html",params)