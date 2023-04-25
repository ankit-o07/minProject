from django.shortcuts import render ,redirect

# Create your views here.
from .form import AddUser , AddDoctor , AddLab ,AddPatient , AddPharmacy
from .models import UserProfile, PatientProfile, DoctorProfile, PharmacyProfile, LabProfile 
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .decorators import authenticat_doctor ,authenticat_lab ,authenticat_pharmacy


def adduser(request):

    if request.method == "POST":
        userForm = AddUser()
        data = {
            "from" : AddUser,
            "title": "signup",
            "warning": "renderdetali"
             
        }
        form = AddUser(request.POST)
        print("test1")
        if form.is_valid():
            print("test2")
            firstName = request.POST.get("firstName","")
            lastName = request.POST.get("lastName","")
            Dob =  request.POST.get("Dob","")
            gender = request.POST.get("gender","")
            email = request.POST.get("email","")
            phoneNumber = request.POST.get("phoneNumber","")
            account_type = request.POST.get("account_type","")
            userName = request.POST.get("userName" ,"")
            password = request.POST.get("password" ,"")
            print("test3")
            user_profile = UserProfile.objects.create(firstName=firstName,lastName=lastName,Dob=Dob,gender=gender,email=email,phoneNumber=phoneNumber,account_type=account_type,userName=userName)
            user_profile.save()
            print("test4")
            my_user = User.objects.create_user(userName,email,password)
            my_user.save()
            
        else :
            print("test5")
            return render(request, "account/sigup.html",data)
    print("test6")
    data = {
            "from" : AddUser,
            "title": "signup"
             
        }
    return render(request, "account/sigup.html",data)

@authenticat_doctor
def regDoctor(request):
    if request.method == "POST":
        userForm = AddDoctor()
        data = {
            "from" : AddDoctor,
            "title": "DoctorRegistration",
            "warning": "reEnterDetali"
             
        }
        form = AddDoctor(request.POST ,request.FILES)
        if form.is_valid():
            qualification = form.cleaned_data['qualification']
            id_proof = form.cleaned_data['id_proof']
            degree = form.cleaned_data['degree']
            experience = form.cleaned_data['Experience']
            fee = form.cleaned_data['Fee']
            address = form.cleaned_data['address']
            user = request.user.username 
            
            user_profile = UserProfile.objects.get(userName=request.user.username)
            doctor_profile = DoctorProfile(user=user_profile,qualification=qualification, id_proof=id_proof, degree=degree, Experience=experience, Fee=fee, address=address)

            print(doctor_profile.address)
            print(doctor_profile.Experience)
            print(doctor_profile.fee)
            # doctor_profile.save()
            

            
        else :
            return render(request, "account/sigup.html",data)

    data = {
            "from" : AddDoctor,
            "title": "DoctorRegistration",
             
        }
    return render(request, "account/doctorReg.html",data)

@authenticat_lab
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


@authenticat_pharmacy
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

def login_view(request):
    
    if request.method == "POST":
        
        userName = request.POST.get("username","")
        password = request.POST.get("password","")
        
        print("Username:",userName)
        print("password:",password)
        user = None
        try:
            user = authenticate(request ,username=userName ,password=password)
        except Exception as e:
            print(e)
        print(user)
        if user is  not None:
            print("Test entry")
            login(request,user)
            username = request.user.username 
            
            
            user_profile = UserProfile.objects.get(userName=username)  
            role = user_profile.account_type
            
            if ( role == "D"):
                
                return redirect("/doctor/dashboard/")
            elif(role == "P"):
                
                return redirect("/pharmacy/dashboard/")
            elif(role == "L"):
                print("test3")
                return redirect("/lab/dashboard/")
            else:
                print("test4")
                return redirect('/')
        else:
            print("exit test")
            return redirect('/account/login')
        
    data = {
        "title":"login"
    }
    return render(request,'account/login.html',data)

def logout_view(request):
    logout(request)
    return redirect('/')




            
