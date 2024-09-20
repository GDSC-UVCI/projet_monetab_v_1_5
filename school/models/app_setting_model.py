from django.db import models
from base.helpers.date_time_model import DateTimeModel


class AppSettingModel(DateTimeModel):
    smpt_server = models.CharField(max_length=50)
    smpt_port = models.PositiveIntegerField()
    smpt_username = models.CharField(max_length=50)
    smpt_password = models.CharField(max_length=50)
