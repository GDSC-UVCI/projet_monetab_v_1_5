from django.db import models
from base.models.person_model import PersonModel


# Create your models here.

class StudentModel(PersonModel):
    register = models.CharField(max_length=30, unique=True)
    phone_number_father = models.CharField(unique=True, blank=True, max_length=10)

    def __str__(self):
        
        return f"{self.last_name} - {self.first_name}"

    class Meta:
        verbose_name = "Eleve"
        verbose_name_plural = "Eleves"
