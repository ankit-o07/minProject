from django.shortcuts import render

# Create your views here.

def home_views(request):
    params = {
        "title":"Home"
    }
    return render(request , "patient/home.html",params)

def doctor_views(request):
    params = {
        "title":"Doctor"
    }
    return render(request , "patient/doctor.html",params)

def lab_views(request):
    params = {
        "title":"Lab"
    }
    return render(request , "patient/lab.html",params)

def pharmacy_views(request):
    params = {
        "title":"Pharmacy"
    }
    return render(request , "patient/pharmacy.html",params)

def blog_views(request):
    params = {
        "title":"Blogs"
    }
    return render(request , "patient/blog.html",params)