# domain/services.py
from .models import Patient, HealthMetric

def create_patient(name, date_of_birth, medical_history):
    return Patient.objects.create(name=name, date_of_birth=date_of_birth, medical_history=medical_history)

def log_health_metric(patient, metric_type, metric_value):
    return HealthMetric.objects.create(patient=patient, type=metric_type, value=metric_value)
