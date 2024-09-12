from rest_framework import serializers
from student.models.absence_model import AbsenceModel


class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbsenceModel
        fields = '__all__'

