# adapters/publisher.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from domain.models import HealthMetric

# Example using Django signals
@receiver(post_save, sender=HealthMetric)
def publish_health_metric(sender, instance, **kwargs):
    # Logic to publish the event, e.g., pushing it to a message broker or a websocket
    print(f"New health metric recorded: {instance.type} for {instance.patient.name} with value {instance.value}")

   