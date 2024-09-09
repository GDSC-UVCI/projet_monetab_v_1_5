from django import forms
from base.models.adrress_model import AdressModel

class AdressForm(forms.ModelForm):
    class Meta:
        model = AdressModel
        exclude = ['created_at', 'updated_at','status']