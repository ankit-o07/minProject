from django.shortcuts import render

# Create your views here.

def pharmacy_dashboard_views(request):
    params = {
        "title":"Pharmacy-dashboard"
    }
    return render(request , "pharma/pharmaDashboard.html",params)