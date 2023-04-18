from django.urls import path

from read_data import views

urlpatterns = [
    path('', views.all_movies, name= 'all_movies'),

]
