from django.urls import path
from school.views.school_views import list, add_and_edit, delete


app_name = 'school'
urlpatterns = [

    path('', list, name='list'),
    path('add/', add_and_edit, name='add'),
    path('edit/<int:pk>', add_and_edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete'),



]