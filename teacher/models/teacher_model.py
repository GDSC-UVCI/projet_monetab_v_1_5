from base.models.person_model import PersonModel
from django.db import models

# Create your models here.
class TeacherModel(PersonModel):
    
    available = models.BooleanField()
    speciality = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    class Meta:
        verbose_name = "Profeseur"
        verbose_name_plural = "Professeurs"
