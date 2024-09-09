from django.db import models

from base.helpers.date_time_model import DateTimeModel
from .students_model import StudentModel


# Create your models here.

class StudentsCardsModel(DateTimeModel):
    student= models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    reference = models.CharField(max_length=50)
    expiration_date = models.DateField()
    issue_date = models.DateField()

    def __str__(self):
        return f"{self.absence_number} - {self.absence_date}"

    class Meta:
        verbose_name = "Student Card"
        verbose_name_plural = "Students Cards"
