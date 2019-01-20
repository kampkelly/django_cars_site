from django.urls import path

from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/add', views.create_car, name='create_car'),
    path('cars/save', views.save_car, name='save_car'),
    path('cars/all', views.all_cars, name='all_cars'),
    path('cars/get/<id>', views.view_car, name='view_car'),
    path('cars/edit/<id>', views.edit_car, name='edit_car'),
    path('cars/update/<id>', views.update_car, name='update_car')
]
