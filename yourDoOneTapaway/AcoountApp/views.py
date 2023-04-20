from django.shortcuts import render

# Create your views here.
from .form import AddUser


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