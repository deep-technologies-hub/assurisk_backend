from rest_framework import viewsets
from .models import (PatientProfile, PrestataireSoinsProfile, PharmacieProfile,
                     PoliceAssurance, ReclamationPatient, Traitement, Medicament, Prescription)
from .serializers import (PatientProfileSerializer, PrestataireSoinsProfileSerializer,
                          PharmacieProfileSerializer, PoliceAssuranceSerializer,
                          ReclamationPatientSerializer, TraitementSerializer,
                          MedicamentSerializer, PrescriptionSerializer)

class PatientProfileViewSet(viewsets.ModelViewSet):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer

class PrestataireSoinsProfileViewSet(viewsets.ModelViewSet):
    queryset = PrestataireSoinsProfile.objects.all()
    serializer_class = PrestataireSoinsProfileSerializer

class PharmacieProfileViewSet(viewsets.ModelViewSet):
    queryset = PharmacieProfile.objects.all()
    serializer_class = PharmacieProfileSerializer

class PoliceAssuranceViewSet(viewsets.ModelViewSet):
    queryset = PoliceAssurance.objects.all()
    serializer_class = PoliceAssuranceSerializer

class ReclamationPatientViewSet(viewsets.ModelViewSet):
    queryset = ReclamationPatient.objects.all()
    serializer_class = ReclamationPatientSerializer

class TraitementViewSet(viewsets.ModelViewSet):
    queryset = Traitement.objects.all()
    serializer_class = TraitementSerializer

class MedicamentViewSet(viewsets.ModelViewSet):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
