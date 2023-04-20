from django.shortcuts import render

# Create your views here.

def lab_dashboard_views(request):
    params = {
        "title":"lab-dashboard"
    }
    return render(request , "lab/labDashboard.html",params)