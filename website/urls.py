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
from django.urls import path, include, re_path
from dashboard.views import log_in, log_out

from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from school.views.app_settings_views import appsetting_add

router = routers.DefaultRouter()
#router.register(r'students', student_list, basename='student')

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('login/', log_in, name='login'),
    path('appsetting/', appsetting_add, name='appsetting_add'),
    path('logout/', log_out, name='logout'),
    path('student/', include('student.urls')),
    path('', include('dashboard.urls')),
    path('teacher/', include('teacher.urls')),
    path('user/', include('user.urls')),
    path("report/", include("report.urls")),
    path("school/", include("school.urls")),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
