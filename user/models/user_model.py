from django.contrib.auth.models import AbstractUser
from django.db import models

from base.helpers.date_time_model import DateTimeModel


class UserModel(AbstractUser, DateTimeModel):
    role = models.ForeignKey('user.RoleUserModel', on_delete=models.SET_NULL, null=True)
    school = models.ForeignKey('school.SchoolModel', on_delete=models.CASCADE, null=True)
    pseudo = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role', 'school', 'pseudo']

    def __str__(self):
        return self.pseudo

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"