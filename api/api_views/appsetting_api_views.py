from django.http import JsonResponse
from rest_framework import viewsets

from api.serializers.appsetting_serializers import AppSettingSerializer
from school.models.app_setting_model import AppSettingModel


class AppSettingViewSet(viewsets.ModelViewSet):
    serializer_class = AppSettingSerializer
    queryset = AppSettingModel.objects.all()

