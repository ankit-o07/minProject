from django.shortcuts import render
from AcoountApp.decorators import authenticat_lab
# Create your views here.
@authenticat_lab
def lab_dashboard_views(request):
    params = {
        "title":"lab-dashboard"
    }
    return render(request , "lab/labDashboard.html",params)