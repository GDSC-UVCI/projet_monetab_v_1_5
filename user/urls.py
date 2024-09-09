from django.urls import path, include


urlpatterns = [
    path('', include('user.Urls.user_urls')),
    path('role/', include('user.Urls.role_user_urls')),

]
