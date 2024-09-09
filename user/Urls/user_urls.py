from django.urls import path
from user.views.user_views import index, add_and_edit, change_user_status, search

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_and_edit, name='add'),
    path('edit/<int:pk>/', add_and_edit, name='edit'),
    path('change_status/<int:pk>/<str:action>/', change_user_status, name='change_status'),
    path('search/', search, name='search'),
]