from rest_framework import serializers
from .models import (PatientProfile, PrestataireSoinsProfile, PharmacieProfile,
                     PoliceAssurance, ReclamationPatient, Traitement, Medicament, Prescription)

class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = '__all__'

class PrestataireSoinsProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrestataireSoinsProfile
        fields = '__all__'

class PharmacieProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacieProfile
        fields = '__all__'

class PoliceAssuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceAssurance
        fields = '__all__'

class ReclamationPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReclamationPatient
        fields = '__all__'

class TraitementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traitement
        fields = '__all__'

class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'
