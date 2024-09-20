from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from api.serializers.absence_serializers import AbsenceSerializer
from student.models.absence_model import AbsenceModel


class AbsenceViewset(viewsets.ModelViewSet):
    serializer_class = AbsenceSerializer
    queryset = AbsenceModel.objects.all()


# @csrf_exempt
# def absence_list(request):
#     if request.method == 'GET':
#         absence = AbsenceModel.objects.all()
#         serializer = AbsenceSerializer(absence, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = AbsenceSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


