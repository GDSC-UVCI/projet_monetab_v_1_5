from django.urls import path
from .views import index, generate_pdf, generate_excel

app_name = 'report'

urlpatterns = [
    path('', index, name='index'),
    path('pdf/<str:report_type>/', generate_pdf, name='generate_pdf'),
    path('excel/<str:report_type>/', generate_excel, name='generate_excel'),
]