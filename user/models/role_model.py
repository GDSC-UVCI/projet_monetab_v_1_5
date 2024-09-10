from django.db import models

from base.helpers.date_time_model import DateTimeModel

# TODO: role and user are not related with many to many relationship

# Create your models here.
class RoleUserModel(DateTimeModel):
    role = models.CharField(max_length=50)
    
    def __str__(self):
        return self.role
    class Meta:
        verbose_name = "Role User"
        verbose_name_plural = "Role Users"
