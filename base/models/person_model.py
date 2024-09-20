from django.db import models
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string

from base.models.gender_enum import GenderModel
from base.helpers.date_time_model import DateTimeModel


class PersonModel(DateTimeModel):
    
    user = models.OneToOneField('user.UserModel',on_delete=models.CASCADE, null=True, blank=True)
    address = models.OneToOneField('base.AddressModel', on_delete=models.CASCADE, null=True, blank=True)
    birthday = models.DateField()
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    phone_number  =models.CharField(max_length=10, unique=True)
    url_picture = models.CharField(max_length=120, null=True, blank=True)
    gender = models.CharField(max_length=1,choices=GenderModel.choices,verbose_name='Genre')
    slug = models.SlugField(default="", unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            unique_slug = get_random_string(length=32)
            self.slug = slugify(unique_slug)

        super(PersonModel, self).save(*args, **kwargs)