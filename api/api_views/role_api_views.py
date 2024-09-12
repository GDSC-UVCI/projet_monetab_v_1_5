from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api.serializers.role_serializers import RoleSerializer
from user.models.role_model import RoleUserModel


@csrf_exempt
def role_list(request):
    if request.method == 'GET':
        roles = RoleUserModel.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RoleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)