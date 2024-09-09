from django.urls import path
from user.views.role_user_views import list, add_and_edit, delete

app_name = 'role'

urlpatterns = [
    path('', list, name='list'),
    path('add/', add_and_edit, name='add'),
    path('edit/<int:pk>/', add_and_edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),

]
