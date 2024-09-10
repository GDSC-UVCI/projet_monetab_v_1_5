from django import forms

from school.models.app_setting_model import AppSettingModel


class AppSettingsForms(forms.ModelForm):

    class Meta:
        model = AppSettingModel
        exclude = ['status']
        #create widgets to beatify the form
