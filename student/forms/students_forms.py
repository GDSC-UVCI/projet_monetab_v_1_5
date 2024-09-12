from django import forms
from student.models.students_model import StudentModel as Student




class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['created_at', 'updated_at', 'address', 'status', ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class':'form-control'}),
            'birthday': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Date of Birth', 'class':'form-control'}),
            'phone_number': forms.NumberInput(attrs={'min': '0', 'placeholder': 'Number', 'class':'form-control'}),
            'phone_number_father': forms.NumberInput(attrs={'min': '0', 'placeholder': 'Number Father', 'class':'form-control'}),
            'url_picture': forms.TextInput(attrs={'placeholder': 'URL Picture','class':'form-control'}),
            'register': forms.TextInput(attrs={'placeholder': 'Register', 'class':'form-control'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-control'}),
        }
