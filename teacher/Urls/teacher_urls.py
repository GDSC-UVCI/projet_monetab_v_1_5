from django.urls import path
from teacher.views.teacher_views import index, add_and_edit, delete

app_name = 'teacher'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_and_edit, name='add'),
    path('edit/<int:pk>/', add_and_edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),

]