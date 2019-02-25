from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    path('<int:user_id>/', views.posts_index, name='posts_index'),
    path('blogs/<int:user_id>/<int:post_id>', views.post_view, name='post_view'),
]