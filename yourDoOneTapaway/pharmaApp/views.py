from django.shortcuts import render
from AcoountApp.decorators import authenticat_pharmacy
# Create your views here.
@authenticat_pharmacy
def pharmacy_dashboard_views(request):
    params = {
        "title":"Pharmacy-dashboard"
    }
    return render(request , "pharma/pharmaDashboard.html",params)