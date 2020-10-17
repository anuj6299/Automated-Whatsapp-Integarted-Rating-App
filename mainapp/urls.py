from django.urls import path, include
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('thanks/', views.thanks, name='thanks'),
    path('check-ratings/', views.check_ratings, name='check_ratings'), 
]
