# api/serializers.py
from rest_framework import serializers
from domain.models import Patient, HealthMetric

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'date_of_birth', 'medical_history']

class HealthMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetric
        fields = ['id', 'patient', 'type', 'value', 'recorded_at']
