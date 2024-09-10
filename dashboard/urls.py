from django.urls import path
from .views import index, check_initial_setup

app_name = 'dashboard'

urlpatterns = [
    path('', check_initial_setup, name='check_initial_setup'),
    path('dashboard/', index, name='index'),
]