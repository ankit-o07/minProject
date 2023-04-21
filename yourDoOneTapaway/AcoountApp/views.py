from django.shortcuts import render

# Create your views here.
from .form import AddUser , AddDoctor , AddLab ,AddPatient , AddPharmacy



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
        form = AddDoctor(request.POST ,request.FILES)
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
    return render(request, "account/doctorReg.html",data)


def regLab(request):
    if request.method == "POST":
        userForm = AddLab()
        data = {
            "from" : AddLab,
            "title": "LabRegistration",
            "warning": "renderdetali"      
        }
        form = AddLab(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            userName = request.POST.get("labName" ,"")
            
            print("username: ", userName)
            
            
        else :
            print("I am lab else")

            return render(request, "account/sigup.html",data)

    data = {
            "from" : AddLab,
            "title": "LabRegistration",
             
        }
    return render(request, "account/labReg.html",data)



def regpharmacy(request):
    if request.method == "POST":
        userForm = AddPharmacy()
        data = {
            "from" : AddPharmacy,
            "title": "LabRegistration",
            "warning": "reEnterdetali"
             
        }
        form = AddPharmacy(request.POST ,request.FILES)
        if form.is_valid():
            userName = request.POST.get("pharmacyName" ,"")
            
            print("username: ", userName)
            
            
        else :
            print("I am pharam else")
            return render(request, "account/sigup.html",data)

    data = {
            "from" : AddPharmacy,
            "title": "LabRegistration",
             
        }
    return render(request, "account/pharmaReg.html",data)