# tests/test_repository.py
from django.test import TestCase
from domain.models import Patient
from adapters.repository import PatientRepository

class PatientRepositoryTest(TestCase):
    def setUp(self):
        self.repository = PatientRepository()
        self.patient = Patient.objects.create(
            name='John Doe', 
            date_of_birth='1990-01-01', 
            medical_history='No known allergies.'
        )
    
    def test_get_patient_by_id(self):
        patient = self.repository.get_by_id(self.patient.id)
        self.assertIsNotNone(patient)
        self.assertEqual(patient.name, 'John Doe')

    def test_save_patient(self):
        new_patient = Patient(
            name='Jane Smith', 
            date_of_birth='1985-05-05', 
            medical_history='Asthma'
        )
        self.repository.save(new_patient)
        self.assertIsNotNone(new_patient.id)
        self.assertEqual(Patient.objects.count(), 2)
