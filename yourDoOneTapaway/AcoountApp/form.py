from django.forms import ModelForm
from .models import DoctorProfile ,UserProfile, LabProfile, PatientProfile, PharmacyProfile
from django import forms

class AddUser(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['firstName', 'lastName',  'Dob', 'gender', 'email', 'phoneNumber', 'account_type','userName']
        widgets = {
            'Dob': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'password': forms.TextInput(attrs={'type':'password'})
        }


class AddPatient(ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['bloodPressure', 'diabetes', 'address']


class AddDoctor(ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['qualification', 'id_proof', 'degree', 'Experience', 'Fee', 'address']


class AddPharmacy(ModelForm):
    class Meta:
        model = PharmacyProfile
        fields = ['pharmacyName', 'license', 'pharmacyAddress']


class AddLab(ModelForm):
    class Meta:
        model = LabProfile
        fields = ['labName', 'license', 'labAddress']


