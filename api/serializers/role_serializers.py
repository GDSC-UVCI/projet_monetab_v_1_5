from rest_framework import serializers
from user.models.role_model import RoleUserModel


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleUserModel
        fields = '__all__'

