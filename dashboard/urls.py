from django.urls import path
from .views import index, log_in, log_out
app_name = 'dashboard'
urlpatterns = [
    path('', index, name='index'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
]