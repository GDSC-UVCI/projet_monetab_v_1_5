from django.urls import path, include



urlpatterns = [
    path('', include('student.Urls.students_urls')),
    path('cards/', include('student.Urls.students_cards_urls')),
    path('absence/', include('student.Urls.absence_urls')),

]
