import os
import django

# Configurer les paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from user.models.user_model import UserModel
from django.contrib.auth.hashers import make_password

class CreateDefaultUser:


    def create_default_user(self, pseudo, password):
        if UserModel.objects.filter(pseudo=pseudo).exists():
            print('Default user already exists')
            return
        try:
            user=UserModel.objects.create_user(pseudo)
            user.save()
            user.password=password
            user.set_password(user.password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            print('Default user created')
        except Exception as e:
            print(f"Default user creation failed : {e}")
