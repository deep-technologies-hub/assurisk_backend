from django.contrib import admin
from .models import Medicament, PatientProfile, PharmacieProfile, PrestataireSoinsProfile, Traitement, ReclamationPatient, Prescription, PoliceAssurance

admin.site.register(Medicament)
admin.site.register(PatientProfile)
admin.site.register(PharmacieProfile)
admin.site.register(PrestataireSoinsProfile)
admin.site.register(Traitement)
admin.site.register(ReclamationPatient)
admin.site.register(Prescription)
admin.site.register(PoliceAssurance)