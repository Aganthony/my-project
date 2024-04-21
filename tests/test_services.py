# tests/test_services.py
from django.test import TestCase
from domain.models import Patient, HealthMetric
from domain.services import create_patient, log_health_metric

class PatientServicesTest(TestCase):
    
    def test_create_patient(self):
        patient = create_patient('Jane Doe', '1988-02-02', 'Diabetes')
        self.assertEqual(patient.name, 'Jane Doe')
        self.assertEqual(Patient.objects.count(), 1)

class HealthMetricServicesTest(TestCase):
    
    def setUp(self):
        self.patient = Patient.objects.create(name='John Doe', date_of_birth='1990-01-01', medical_history='No known allergies.')
        
    def test_log_health_metric(self):
        metric = log_health_metric(self.patient, 'Blood Pressure', 120)
        self.assertEqual(metric.type, 'Blood Pressure')
        self.assertEqual(metric.value, 120)
        self.assertEqual(HealthMetric.objects.count(), 1)
