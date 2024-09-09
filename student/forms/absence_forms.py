from django import forms
from student.models.absence_model import AbsenceModel as Absence
from datetime import datetime


class AbsenceForm(forms.ModelForm):

    class Meta:
        model = Absence
        fields = ['absence_date','student','absence_number']
        widgets = {
            'absence_date': forms.DateInput(attrs={'type': 'date'}),
            'absence_number': forms.NumberInput(),
        }
      