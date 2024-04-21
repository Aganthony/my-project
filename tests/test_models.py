# tests/test_models.py
from django.test import TestCase
from domain.models import Patient

class PatientModelTests(TestCase):
    def test_create_patient(self):
        patient = Patient.objects.create(name='John Doe', date_of_birth='1990-01-01', medical_history='None')
        self.assertEqual(patient.name, 'John Doe')
