

# from api.api_views.student_api_views import student_list, student_detail
# from api.api_views.user_api_views import users_list, users_detail
# #from api.api_views.teacher_api_views import teacher_list, teacher_detail

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.api_views.student_api_views import StudentViewset
from api.api_views.teacher_api_views import TeacherViewset
from api.api_views.user_api_views import UserViewset

router = DefaultRouter()
router.register('students', StudentViewset)
router.register('users', UserViewset)
router.register('teachers', TeacherViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #path('students/', student_list, name='student_list'),
    #path('students/<int:pk>/', student_detail, name='student_detail'),
    #path('teachers/', teacher_list, name='teacher_list'),
    # path('teachers/<int:pk>/', teacher_detail, name='teacher_detail'),
    # path('users/', users_list, name='user_list'),
    # path('users/<int:pk>/', users_detail, name='user_detail'),


]