# api/urls.py
from django.urls import path
from .views import health_metric_log

urlpatterns = [
   
    path('metrics/log/<int:patient_id>', health_metric_log, name='health-metric-log'),
]
