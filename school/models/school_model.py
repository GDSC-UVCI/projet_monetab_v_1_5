from django.db import models
from base.helpers.named_date_time_model import NamedDateTimeModel
from school.models.app_setting_model import AppSettingModel


class SchoolModel(NamedDateTimeModel):
    app_setting = models.ForeignKey(AppSettingModel, on_delete=models.CASCADE)
    url_logo = models.CharField(max_length=50)
