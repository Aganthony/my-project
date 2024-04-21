# adapters/repository.py
from domain.models import Patient

class PatientRepository:
    def get_by_id(self, id):
        return Patient.objects.get(pk=id)

    def save(self, patient):
        patient.save()
