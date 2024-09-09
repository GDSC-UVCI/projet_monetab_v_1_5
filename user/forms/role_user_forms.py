from django import forms
from user.models.role_model import RoleUserModel as Role


class RoleUserForm(forms.ModelForm):
        
    class Meta:
        model = Role
        fields = ["role"]
        
        
