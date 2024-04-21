# domain/models.py
from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    medical_history = models.TextField()

    def __str__(self):
        return self.name

class HealthMetric(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    value = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} for {self.patient.name}: {self.value}"

