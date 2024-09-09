from django.db import models
from django.utils.translation import gettext_lazy as _



class GenderModel(models.TextChoices):
    MALE = "H", _("Homme") 
    FEMALE = "F", _("Femme")
    OTHER = "O", _("Autre")

    