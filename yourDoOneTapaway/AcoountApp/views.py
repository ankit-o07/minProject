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
            "form" : AddUser,
            "title": "signup",
            "warning": "ReEnter Details"
             
        }
        form = AddUser(request.POST)
        print(form.is_valid())

        if form.is_valid():

            firstName = form.cleaned_data["firstName"]
            lastName = form.cleaned_data["lastName"]
            Dob = form.cleaned_data["Dob"]
            gender = form.cleaned_data["gender"]
            email = form.cleaned_data["email"]
            phoneNumber = form.cleaned_data["phoneNumber"]
            account_type = form.cleaned_data["account_type"]
            userName = form.cleaned_data["userName"]
            
            password = request.POST.get("password","")
            user_profile = UserProfile.objects.create(firstName=firstName, lastName=lastName, Dob=Dob, gender=gender, email=email, phoneNumber=phoneNumber, account_type=account_type, userName=userName)
            
            
            user_profile.save()

            my_user = User.objects.create_user(userName,email,password)
            my_user.save()
            return redirect('/')
            
        else :
            print(form.errors)
            return render(request, "account/sigup.html",data)

    data = {
            "form" : AddUser,
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
            print(doctor_profile.Fee)
            print(doctor_profile.user.firstName)
            print(doctor_profile.user.email)
            doctor_profile.save()
            data= {
                "name":doctor_profile.user.firstName,
                "fee":doctor_profile.Fee
            }
            return redirect('/doctor/doctorDashboard/')
            

            
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
            "warning": "<h1>Re Enter detail</h1>"  
        }
        form = AddLab(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            labName = request.POST.get("labName" ,"")
            license = form.cleaned_data["license"]
            labAddress = form.cleaned_data["labAddress"]

            user_profile = UserProfile.objects.get(userName=request.user.username)
            lab_profile = LabProfile(user= user_profile,license=license, labName=labName , labAddress= labAddress)    
            lab_profile.save()        
            print(form.errors)
            return redirect('/lab/dashboard')
        else :
            print("I am lab else")
            data['form'] = form
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
            pharmacyName = request.POST.get("pharmacyName" ,"")
            license = form.cleaned_data["license"]
            pharmacyAddress = form.cleaned_data["pharmacyAddress"]
            user_profile = UserProfile.objects.get(userName=request.user.username)
            pharmacy_profile = PharmacyProfile(user= user_profile,pharmacyName=pharmacyName,license=license,pharmacyAddress=pharmacyAddress)
            pharmacy_profile.save()
            return redirect('/pharma/pharmadashboard')
            
            
        else :
            print("I am pharam else")
            return render(request, "account/sigup.html",data)

    data = {
            "from" : AddPharmacy,
            "title": "LabRegistration",
             
        }
    return render(request, "account/pharmaReg.html",data)


def  Regpatient(request):
    if request.method == "POST":
        userForm = AddPatient() 
        data = {
            "form" :AddPatient,
            "title": "Patient Registration",
            "warning": "ReEnterdetali"

        }
        form = AddPatient(request.POST)
        if form.is_valid():
            bloodPressure = form.cleaned_data["bloodPressure"]
            diabetes = form.cleaned_data["diabetes"]
            address = form.cleaned_data["address"]

            user_profile = UserProfile.objects.get(userName=request.user.username)
            patient_profile = PatientProfile(user= user_profile,bloodPressure=bloodPressure,diabetes=diabetes,address=address)
            patient_profile.save()
            return redirect("/")
        else :
            return render(request,)
    userForm = AddPatient() 
    data = {
        "form" :AddPatient,
        "title": "Patient Registration",
        "warning": "ReEnterdetali"

    }
    return render(request,"account/patientReg.html",data)

            


def login_view(request):
    
    if request.method == "POST":
        
        userName = request.POST.get("username","")
        password = request.POST.get("password","")
        
        print("Username:",userName)
        print("password:",password)
        
        user = authenticate(request,username=userName, password=password)
        
        print(user)
        if user is  not None:
            print("Test entry")
            login(request,user)
            username = request.user.username 
            print("username: ", username)
            
            
            user_profile = UserProfile.objects.get(userName=username)  
            role = user_profile.account_type
            print(role)
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




            
