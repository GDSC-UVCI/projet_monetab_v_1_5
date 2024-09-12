from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api.serializers.address_serializers import AddressSerializer
from base.models.address_model import AddressModel


@csrf_exempt
def address_list(request):
    if request.method == 'GET':
        address = AddressModel.objects.all()
        serializer = AddressSerializer(address, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


