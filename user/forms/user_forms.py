from django import forms
from user.models.user_model import UserModel as User

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance is not None:
            self.fields['pseudo'].widget.attrs.update({
                'readonly': 'readonly',
                'label': 'azy'
            })
            self.fields['password'].required = False

        self.fields['pseudo'].help_text = ''
        self.fields['pseudo'].required = False
        self.fields['password'].required = False

    class Meta:
        model = User
        fields = ["username", "pseudo", "password", "role", "school", "is_active"]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'pseudo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your pseudo'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        }