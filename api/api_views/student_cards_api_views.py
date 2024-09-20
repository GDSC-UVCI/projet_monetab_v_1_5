from rest_framework import viewsets

from api.serializers.student_cards_serializers import StudentsCardsSerializer
from student.models.students_cards_model import StudentsCardsModel


class StudentCardsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentsCardsSerializer
    queryset = StudentsCardsModel.objects.all()