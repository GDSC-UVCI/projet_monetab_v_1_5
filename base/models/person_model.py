from django.db import models
from base.models.gender_enum import GenderModel
from base.helpers.date_time_model import DateTimeModel


class PersonModel(DateTimeModel):
    
    user = models.OneToOneField('user.UserModel',on_delete=models.CASCADE, null=True, blank=True)
    adress = models.OneToOneField('base.AdressModel',on_delete=models.CASCADE, null=True, blank=True)
    birthday = models.DateField()
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    phone_number  =models.CharField(max_length=10, unique=True)
    url_picture = models.CharField(max_length=120, null=True, blank=True)
    gender = models.CharField(max_length=1,choices=GenderModel.choices,verbose_name='Genre')

    class Meta:
        abstract = True