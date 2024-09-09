from django import forms
from student.models.students_model import StudentModel as Student

# CLASS = [
#     ('', ' Selectionnez une classe'),
#     ('Tle', 'Tle'),
#     ('1ère', '1ère'),
#     ('2nd', '2nd'),
#     ('3ème', '3ème'),
#     (' 4ème', '4ème'),
#     ('5ème', '5ème'),
#     ('6ème', '6ème')
# ]

# GENDER = [
#     (True, 'Homme'),
#     (False, 'Femme')
# ]

# # class StudentForm(forms.Form):
# #     CLASS = [
# #         (' Selectionnez une classe', ' Selectionnez une classe'),
# #         ('Tle', 'Tle'),
# #         ('1ère', '1ère'),
# #         ('2nd', '2nd'),
# #         ('3ème', '3ème'),
# #         (' 4ème', '4ème'),
# #         ('5ème', '5ème'),
# #         ('6ème', '6ème')
# #     ]
# #     GENDER = [
# #         ('0', 'Homme'),
# #         ('1', 'Femme')
# #     ]
# #     first_name = forms.CharField(required=True)
# #     last_name = forms.CharField(widget=forms.TextInput(
# #         attrs={
# #             'placeholder': 'MON NOM',
# #             'class':'name'

# #         }
# #     ))
# #     birth_date = forms.DateField(widget=forms.DateInput(
# #         attrs={
# #             'type':'date',
# #             'placeholder':'Date of Birth',

# #         }
# #     ))
# #     classroom = forms.ChoiceField(choices=CLASS)
# #     phone = forms.CharField(widget=forms.NumberInput(
# #         attrs={
# #             'min':'1',
# #             'placeholder':'Number'
# #         }))
# #     city = forms.CharField(max_length=20,widget=forms.TextInput(
# #         attrs={
# #             'placeholder':'City'
# #         }
# #     ))
# #     register = forms.CharField(widget=forms.TextInput(
# #         attrs={
# #             'placeholder':'Register'
# #         }

# #     ))
# #     gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect())

# gender = forms.BooleanField(widget=forms.RadioSelect(choices=GENDER))


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['created_at', 'updated_at','adress','status',]
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
