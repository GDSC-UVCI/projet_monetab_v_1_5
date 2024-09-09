from django.urls import path
from student.views.students_views import index, add_and_edit, delete

app_name = 'student'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_and_edit, name='add'),
    path('edit/<int:pk>/', add_and_edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),

]
