from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from base.helpers.date_time_model import DateTimeModel
class UserModel(AbstractUser, DateTimeModel):

    role = models.ManyToManyField('user.RoleUserModel', blank=True)
    school = models.ForeignKey('school.SchoolModel', on_delete=models.CASCADE, null=True)
    pseudo = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Add this line
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role', 'school', 'pseudo']

    def __str__(self):
        return self.pseudo

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"