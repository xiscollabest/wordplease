from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    path('blogs/<str:username>/', views.posts_index, name='posts_index'),
    path('blogs/<str:username>/<int:post_id>', views.post_view, name='post_view'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)