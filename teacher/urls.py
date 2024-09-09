from django.urls import path, include


urlpatterns = [
    path('', include('teacher.Urls.teacher_urls')),

]