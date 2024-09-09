from django.db import models
from base.helpers.named_date_time_model import NamedDateTimeModel

class SchoolModel(NamedDateTimeModel):
    app_setting = models.ForeignKey('school.AppSettingModel',on_delete=models.CASCADE,related_name='school_app_id')
    url_logo = models.CharField(max_length=50)
