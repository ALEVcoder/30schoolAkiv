from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('tadbirlar/', views.blog_detail, name='blog'),
]