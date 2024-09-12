from rest_framework import serializers
from student.models.students_cards_model import StudentsCardsModel


class StudentsCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsCardsModel
        fields = '__all__'

