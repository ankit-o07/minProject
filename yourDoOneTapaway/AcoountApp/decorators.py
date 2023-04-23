from django.http import  HttpResponse
from django.shortcuts import render,redirect
from .models import UserProfile, PatientProfile, DoctorProfile, PharmacyProfile, LabProfile 


def user_is_authenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else :
            return view_func(request , *args , **kwargs)
    return wrapper_func



def authenticat_doctor(view_func):
    def wrapper_func(request , *args , **kwargs):
        username = request.user.username            
        user_profile = UserProfile.objects.get(userName=username)  
        role = user_profile.account_type

        if (role != "D"):
            return HttpResponse("<h1>you do not have permission to access this page</h1>")
        else:
            return view_func(request , *args , **kwargs)
    return wrapper_func


def authenticat_lab(view_func):
    def wrapper_func(request , *args , **kwargs):
        username = request.user.username            
        user_profile = UserProfile.objects.get(userName=username)  
        role = user_profile.account_type

        if (role != "L"):
            return HttpResponse("<h1>you do not have permission to access this page</h1>")
        else:
            return view_func(request , *args , **kwargs)
    return wrapper_func

def authenticat_pharmacy(view_func):
    def wrapper_func(request , *args , **kwargs):
        username = request.user.username            
        user_profile = UserProfile.objects.get(userName=username)  
        role = user_profile.account_type

        if (role != "P"):
            return HttpResponse("<h1>you do not have permission to access this page</h1>")
        else:
            return view_func(request , *args , **kwargs)
    return wrapper_func
