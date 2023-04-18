from django.urls import path

from read_data import views

urlpatterns = [
    path('', views.home, name= 'index'),

]
