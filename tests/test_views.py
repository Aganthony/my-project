# tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from domain.models import Patient, HealthMetric
from datetime import date

class HealthMetricViewTests(TestCase):
    def setUp(self):
        # Setup run before every test method.
        self.client = Client()
        self.patient = Patient.objects.create(
            name='John Doe',
            date_of_birth=date(1980, 1, 1),
            medical_history='No known allergies.'
        )

    def test_health_metric_logging(self):
        # Simulate POST request to log a health metric
        response = self.client.post(
            reverse('health-metric-log', kwargs={'patient_id': self.patient.id}),
            {
                'type': 'Heart Rate',
                'value': 72
            }
        )

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the health metric was correctly logged.
        self.assertEqual(HealthMetric.objects.count(), 1)
        metric = HealthMetric.objects.first()
        self.assertEqual(metric.type, 'Heart Rate')
        self.assertEqual(metric.value, 72)
        self.assertEqual(metric.patient, self.patient)

   