"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dashboard.views import log_in, log_out
from api.api_views.student_api_views import student_list
from rest_framework import routers

from school.views.app_settings_views import appsetting_add

router = routers.DefaultRouter()
#router.register(r'students', student_list, basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/', student_list, name='student_list'),
    path('login/', log_in, name='login'),
    path('appsetting/', appsetting_add, name='appsetting_add'),
    path('logout/', log_out, name='logout'),
    path('student/', include('student.urls')),
    path('', include('dashboard.urls')),
    path('teacher/', include('teacher.urls')),
    path('user/', include('user.urls')),
    path("report/", include("report.urls")),
    path("school/", include("school.urls")),


]
