from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'patients', views.PatientProfileViewSet)
router.register(r'prestataires', views.PrestataireSoinsProfileViewSet)
router.register(r'pharmacies', views.PharmacieProfileViewSet)
router.register(r'polices', views.PoliceAssuranceViewSet)
router.register(r'reclamations', views.ReclamationPatientViewSet)
router.register(r'traitements', views.TraitementViewSet)
router.register(r'medicaments', views.MedicamentViewSet)
router.register(r'prescriptions', views.PrescriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]