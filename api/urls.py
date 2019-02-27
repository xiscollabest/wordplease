from . import views
from django.urls import include, path


urlpatterns = [
    path('users/', views.ListUser.as_view()),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
]