from django.shortcuts import render

# Create your views here.
from .form import AddUser , AddDoctor



def adduser(request):


    if request.method == "POST":
        userForm = AddUser()
        data = {
            "from" : AddUser,
            "title": "signup",
            "warning": "renderdetali"
             
        }
        form = AddUser(request.POST)
        if form.is_valid():
            userName = request.POST.get("userName" ,"")
            password = request.POST.get("password" ,"")
            print("username: ", userName)
            print("password: ", password)
        else :
            return render(request, "account/sigup.html",data)

    data = {
            "from" : AddUser,
            "title": "signup"
             
        }
    return render(request, "account/sigup.html",data)


def regDoctor(request):
    if request.method == "POST":
        userForm = AddDoctor()
        data = {
            "from" : AddDoctor,
            "title": "DoctorRegistration",
            "warning": "renderdetali"
             
        }
        form = AddUser(request.POST)
        if form.is_valid():
            userName = request.POST.get("Fee" ,"")
            password = request.POST.get("Experience" ,"")
            print("username: ", userName)
            print("password: ", password)
        else :
            return render(request, "account/sigup.html",data)

    data = {
            "from" : AddDoctor,
            "title": "DoctorRegistration",
             
        }
    return render(request, "account/docReg.html",data)
