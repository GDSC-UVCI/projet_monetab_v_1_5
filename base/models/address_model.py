from django.db import models
from base.helpers.date_time_model import DateTimeModel

class AddressModel(DateTimeModel):
    city =models.CharField(max_length=50)
    street =models.CharField(max_length=50)
    country =models.CharField(max_length=50)

    def __str__(self) :
        return f"{self.city}-{self.country}"