

# from api.api_views.student_api_views import student_list, student_detail
# from api.api_views.user_api_views import users_list, users_detail
# #from api.api_views.teacher_api_views import teacher_list, teacher_detail

from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from api.api_views.absence_api_views import AbsenceViewset
from api.api_views.address_api_views import AddressViewSet
from api.api_views.appsetting_api_views import AppSettingViewSet
from api.api_views.role_api_views import RoleViewSet
from api.api_views.school_api_views import SchoolViewSet
from api.api_views.student_api_views import StudentViewset
from api.api_views.student_cards_api_views import StudentCardsViewSet
from api.api_views.teacher_api_views import TeacherViewset
from api.api_views.user_api_views import UserViewset
from student.models.students_cards_model import StudentsCardsModel

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

router = DefaultRouter()
router.register('students', StudentViewset)
router.register('users', UserViewset)
router.register('teachers', TeacherViewset)
router.register(r'absences', AbsenceViewset)
router.register(r'address', AddressViewSet)
router.register(r'appsettings', AppSettingViewSet)
router.register(r'student_card', StudentCardsViewSet)
router.register(r'schools', SchoolViewSet)
router.register(r'roles', RoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    #path('students/', student_list, name='student_list'),
    #path('students/<int:pk>/', student_detail, name='student_detail'),
    #path('teachers/', teacher_list, name='teacher_list'),
    # path('teachers/<int:pk>/', teacher_detail, name='teacher_detail'),
    # path('users/', users_list, name='user_list'),
    # path('users/<int:pk>/', users_detail, name='user_detail'),


]