

from api.api_views.student_api_views import student_list, student_detail
from api.api_views.user_api_views import users_list
from api.api_views.teacher_api_views import teacher_list

from django.urls import path

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('students/<int:pk>/', student_detail, name='student_detail'),
    path('teachers/', teacher_list, name='teacher_list'),
    path('users/', users_list, name='user_list'),


]