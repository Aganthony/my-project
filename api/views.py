# api/views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from domain.services import create_patient, log_health_metric
from tests.test_models import Patient

def patient_create(request):
    # You should use Django's forms or serializers to handle validation.
    patient = create_patient(request.POST['name'], request.POST['date_of_birth'], request.POST['medical_history'])
    return JsonResponse({'id': patient.id, 'name': patient.name})

def health_metric_log(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    metric = log_health_metric(patient, request.POST['type'], request.POST['value'])
    return JsonResponse({'id': metric.id, 'type': metric.type, 'value': metric.value})
