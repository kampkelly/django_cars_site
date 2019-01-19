from django.urls import path

from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/add', views.create_car, name='create_car'),
    path('cars/save', views.save_car, name='save_car'),
    path('cars/all', views.all_cars, name='all_cars'),
]
