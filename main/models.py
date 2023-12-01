from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numero_d_assurance_sociale = models.CharField(max_length=50)
    date_de_naissance = models.DateField()
    sexe = models.CharField(max_length=10)
    adresse = models.TextField()
    numero_de_telephone = models.CharField(max_length=20, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])

    def __str__(self):
        return self.user.username

class PrestataireSoinsProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    numero_de_telephone = models.CharField(max_length=20, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])

    def __str__(self):
        return self.nom

class PharmacieProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    numero_de_telephone = models.CharField(max_length=20, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])

    def __str__(self):
        return self.nom

class PoliceAssurance(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    date_de_debut = models.DateField()
    date_de_fin = models.DateField()
    type_de_couverture = models.CharField(max_length=100)
    prime = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.patient.user.username} - {self.type_de_couverture}"

class ReclamationPatient(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    date = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"Réclamation de {self.patient.user.username} - {self.statut}"

class Traitement(models.Model):
    prestataire = models.ForeignKey(PrestataireSoinsProfile, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    date = models.DateField()
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    montant_reclame = models.DecimalField(max_digits=10, decimal_places=2)
    statut_reclamation = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"Traitement pour {self.patient.user.username} par {self.prestataire.nom}"

class Medicament(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    nombre = models.IntegerField(default=0)

    def __str__(self):
        return self.nom

    def prix_total(self):
        return self.prix * self.nombre

class Prescription(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    pharmacie = models.ForeignKey(PharmacieProfile, on_delete=models.CASCADE)
    date = models.DateField()
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    montant_reclame = models.DecimalField(max_digits=10, decimal_places=2)
    statut_reclamation = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"Prescription de {self.medicament.nom} pour {self.patient.user.username}"
