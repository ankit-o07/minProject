from django.contrib import admin
from .models import DoctorProfile ,UserProfile, LabProfile, PatientProfile, PharmacyProfile

# Register your models here.
admin.site.register(DoctorProfile)
admin.site.register(UserProfile)
admin.site.register(LabProfile)
admin.site.register(PatientProfile)
admin.site.register(PharmacyProfile
)