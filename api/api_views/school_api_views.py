from rest_framework import viewsets

from api.serializers.school_serializers import SchoolSerializer
from school.models.school_model import SchoolModel


class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = SchoolModel.objects.all()