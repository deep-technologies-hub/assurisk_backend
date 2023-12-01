from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import PatientProfile, PrestataireSoinsProfile, PharmacieProfile
from .serializers import PatientProfileSerializer, PrestataireSoinsProfileSerializer, PharmacieProfileSerializer

from .models import (PatientProfile, PrestataireSoinsProfile, PharmacieProfile,
                     PoliceAssurance, ReclamationPatient, Traitement, Medicament, Prescription)
from .serializers import (PatientProfileSerializer, PrestataireSoinsProfileSerializer,
                          PharmacieProfileSerializer, PoliceAssuranceSerializer,
                          ReclamationPatientSerializer, TraitementSerializer,
                          MedicamentSerializer, PrescriptionSerializer)


class PatientProfileViewSet(viewsets.ModelViewSet):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer

    # def create(self, request, *args, **kwargs):
    #     user_data = request.data.pop('user')  # Informations de l'utilisateur
    #     user = User.objects.create_user(**user_data)
    #     patient_serializer = self.get_serializer(data=request.data)
    #
    #     if patient_serializer.is_valid():
    #         patient_serializer.save(user=user)
    #         return Response(patient_serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         user.delete()  # Supprime l'utilisateur si la création du patient échoue
    #         return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrestataireSoinsProfileViewSet(viewsets.ModelViewSet):
    queryset = PrestataireSoinsProfile.objects.all()
    serializer_class = PrestataireSoinsProfileSerializer

    # def create(self, request, *args, **kwargs):
    #     user_data = request.data.pop('user')  # Informations de l'utilisateur
    #     user = User.objects.create_user(**user_data)
    #     prestataire_serializer = self.get_serializer(data=request.data)
    #
    #     if prestataire_serializer.is_valid():
    #         prestataire_serializer.save(user=user)
    #         return Response(prestataire_serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         user.delete()  # Supprime l'utilisateur si la création échoue
    #         return Response(prestataire_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PharmacieProfileViewSet(viewsets.ModelViewSet):
    queryset = PharmacieProfile.objects.all()
    serializer_class = PharmacieProfileSerializer

    # def create(self, request, *args, **kwargs):
    #     user_data = request.data.pop('user')  # Informations de l'utilisateur
    #     user = User.objects.create_user(**user_data)
    #     pharmacie_serializer = self.get_serializer(data=request.data)
    #
    #     if pharmacie_serializer.is_valid():
    #         pharmacie_serializer.save(user=user)
    #         return Response(pharmacie_serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         user.delete()  # Supprime l'utilisateur si la création échoue
    #         return Response(pharmacie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
