from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_posts_view, name='index'),
    path('new/', views.new_post_view, name='new_post')
]
