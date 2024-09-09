from django.db import models

from base.helpers.date_time_model import DateTimeModel
from .students_model import StudentModel


# Create your models here.

class AbsenceModel(DateTimeModel):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    absence_date = models.DateField()
    absence_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.absence_number} - {self.absence_date}"

    class Meta:
        verbose_name = "Absence"
        verbose_name_plural = "Absences"
