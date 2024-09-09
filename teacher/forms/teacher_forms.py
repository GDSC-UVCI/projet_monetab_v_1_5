from django import forms
from teacher.models.teacher_model import TeacherModel as Teacher






class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ['user', 'adress', 'created_at', 'updated_at', 'status']
        
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Phone Number','min':'0'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-control'}),
            'speciality': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Speciality'}),
            'url_picture': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Url Picture'}),
            
        }
