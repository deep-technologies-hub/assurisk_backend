from django.db import models
from django.contrib.auth.models import User

# Profil utilisateur pour les Patients
# Ce modèle stocke les informations détaillées des patients.
class PatientProfile(models.Model):
    # Relation un-à-un avec le modèle User de Django pour l'authentification.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Numéro d'assurance sociale du patient, unique pour chaque patient.
    numero_d_assurance_sociale = models.CharField(max_length=50)

    # Date de naissance du patient.
    date_de_naissance = models.DateField()

    # Sexe du patient, peut être stocké comme 'Masculin', 'Féminin', etc.
    sexe = models.CharField(max_length=10)

    # Adresse résidentielle du patient.
    adresse = models.TextField()

    # Numéro de téléphone du patient.
    numero_de_telephone = models.CharField(max_length=20)

# Profil utilisateur pour les Prestataires de Soins
# Ce modèle représente les prestataires de soins comme les cliniques ou les hôpitaux.
class PrestataireSoinsProfile(models.Model):
    # Relation un-à-un avec le modèle User pour l'authentification.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Nom du prestataire de soins.
    nom = models.CharField(max_length=100)

    # Adresse du prestataire de soins.
    adresse = models.TextField()

    # Numéro de téléphone du prestataire de soins.
    numero_de_telephone = models.CharField(max_length=20)

    # Type de prestataire, par exemple 'Clinique', 'Hôpital', etc.
    type = models.CharField(max_length=50)

# Profil utilisateur pour les Pharmacies
# Ce modèle représente les pharmacies.
class PharmacieProfile(models.Model):
    # Relation un-à-un avec le modèle User pour l'authentification.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Nom de la pharmacie.
    nom = models.CharField(max_length=100)

    # Adresse de la pharmacie.
    adresse = models.TextField()

    # Numéro de téléphone de la pharmacie.
    numero_de_telephone = models.CharField(max_length=20)

# Modèle pour les Polices d'Assurance
# Ce modèle stocke les informations sur les polices d'assurance des patients.
class PoliceAssurance(models.Model):
    # Référence au patient associé à la police d'assurance.
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)

    # Date de début de la couverture d'assurance.
    date_de_debut = models.DateField()

    # Date de fin de la couverture d'assurance.
    date_de_fin = models.DateField()

    # Type de couverture d'assurance, par exemple 'Complète', 'Partielle', etc.
    type_de_couverture = models.CharField(max_length=100)

    # Prime d'assurance à payer pour cette police.
    prime = models.DecimalField(max_digits=10, decimal_places=2)

# Modèle pour les Réclamations des Patients
# Ce modèle gère les réclamations d'assurance faites par les patients.
class ReclamationPatient(models.Model):
    # Référence au patient qui fait la réclamation.
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)

    # Date à laquelle la réclamation est faite.
    date = models.DateField()

    # Montant réclamé par le patient.
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    # Statut de la réclamation, par exemple 'En attente', 'Approuvée', 'Rejetée'.
    statut = models.CharField(max_length=50)

    # Description détaillée de la réclamation.
    description = models.TextField()

# Modèle pour les Traitements
# Ce modèle stocke les informations sur les traitements médicaux des patients.
class Traitement(models.Model):
    # Référence au prestataire de soins qui fournit le traitement.
    prestataire = models.ForeignKey(PrestataireSoinsProfile, on_delete=models.CASCADE)

    # Référence au patient recevant le traitement.
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)

    # Date à laquelle le traitement a été fourni.
    date = models.DateField()

    # Coût du traitement.
    cout = models.DecimalField(max_digits=10, decimal_places=2)

    # Montant réclamé pour le traitement (dans le cadre d'une réclamation d'assurance).
    montant_reclame = models.DecimalField(max_digits=10, decimal_places=2)

    # Statut de la réclamation associée au traitement.
    statut_reclamation = models.CharField(max_length=50)

    # Description détaillée de la réclamation liée au traitement.
    description = models.TextField()

# Modèle pour les Médicaments
# Ce modèle représente les médicaments qui peuvent être prescrits.
class Medicament(models.Model):
    # Nom du médicament.
    nom = models.CharField(max_length=100)

    # Description du médicament.
    description = models.TextField()

    # Prix unitaire du médicament.
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    # Quantité de médicament (nombre d'unités).
    nombre = models.IntegerField(default=0)

    # Méthode pour calculer le prix total basé sur le prix unitaire et la quantité.
    def prix_total(self):
        return self.prix * self.nombre

# Modèle pour les Prescriptions
# Ce modèle gère les prescriptions de médicaments pour les patients.
class Prescription(models.Model):
    # Référence au patient à qui la prescription est destinée.
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)

    # Référence au médicament prescrit.
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)

    # Référence à la pharmacie où la prescription peut être remplie.
    pharmacie = models.ForeignKey(PharmacieProfile, on_delete=models.CASCADE)

    # Date de la prescription.
    date = models.DateField()

    # Coût de la prescription.
    cout = models.DecimalField(max_digits=10, decimal_places=2)

    # Montant réclamé pour la prescription (dans le cadre d'une réclamation d'assurance).
    montant_reclame = models.DecimalField(max_digits=10, decimal_places=2)

    # Statut de la réclamation associée à la prescription.
    statut_reclamation = models.CharField(max_length=50)

    # Description détaillée de la réclamation liée à la prescription.
    description = models.TextField()
