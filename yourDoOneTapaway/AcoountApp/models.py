from django.db import models
from django.db.models.fields import Field
from django.contrib.auth.models import User
from django import forms

# Create your models here.
#,verbose_name=""

class UserProfile(models.Model):
    account_type_choices = [("p","Patient"),("D","Doctor"),("L","Laboratory"),("P","pharmacy")]
    gender_choices = [("M", "Male"), ("F", "Female"), ("O", "Other")]

    

    firstName = models.CharField(max_length=100, unique=False)
    lastName = models.CharField(max_length=100, unique=False, blank=True)
    Dob = models.DateField(unique=False)
    gender = models.CharField(max_length=2, choices=gender_choices, blank=True)
    email = models.EmailField(max_length=200,)
    phoneNumber = models.IntegerField()
    account_type = models.CharField(max_length=2,unique=False,choices=account_type_choices)

    userName = models.CharField(max_length=50, unique=False)
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.firstName 



class PatientProfile(models.Model):
    
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)
    bloodPressure_choices = [("H","High"),("L","Low"),("N","Normal")]
    diabetes_choices = [("H","High"),("L","Low"),("N","Normal")]

    
        
    bloodPressure = models.CharField(max_length=2,choices=bloodPressure_choices)
    diabetes = models.CharField(max_length=2 , choices=diabetes_choices)
    address = models.CharField(max_length=500)
    

    
    
    def __str__(self):
        return self.user.firstName
    
class DoctorProfile(models.Model):
    
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)
    qualification= models.CharField(max_length=100,blank=False)
    id_proof = models.FileField()
    degree = models.FileField()
    Experience = models.CharField(max_length=100)
    Fee = models.IntegerField()
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.user.firstName

class PharmacyProfile(models.Model):
    pharmacyId = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    pharmacyName = models.CharField(max_length=100)
    license = models.FileField(upload_to="static")
    pharmacyAddress = models.FileField()
    
    def __str__(self):
        return self.pharmacyName

class LabProfile(models.Model):
    labId = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    labName = models.CharField(max_length=100)
    license = models.FileField()
    labAddress = models.FileField()

    def __str__(self):
        return self.labName
    

  

