from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser

from rest_framework import viewsets
from django.contrib.auth.hashers import make_password
from yaml import serialize

from api.serializers.user_serializers import UserSerializer
from user.models.user_model import UserModel as User


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        if 'password' in data:
            data['password'] = make_password(data['password'])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return JsonResponse(serializer.data, status=201, headers=headers)




# @csrf_exempt
# def users_list(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def users_detail(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return JsonResponse({'error': 'User does not exist'}, status=404)
#
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = UserSerializer(user, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return JsonResponse({'message': 'User was deleted successfully!'}, status=204)


# @csrf_exempt
# def users_detail(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return JsonResponse({'error': 'User does not exist'}, status=404)
#
#     if request.method == 'GET':
#         user = User.objects.get(pk=pk)
#         serializer = UserSerializer(user)
#         return JsonResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         user = User.objects.get(pk=pk)
#         serializer = UserSerializer(user, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return JsonResponse({'message': 'User was deleted successfully!'}, status=204)
#
#
