from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Car
from .helpers.decorators.car_validator import check_for_empty_fields


# Create your views here.
def index(request):
    context = {}
    return render(request, 'cars/index.html', context)


def create_car(request):
    context = {}
    return render(request, 'cars/car/create.html', context)


@check_for_empty_fields
def save_car(request):
    car = Car(name=request.POST['name'], model=request.POST['model'], colour=request.POST['colour'], year=request.POST['year'])
    try:
        car.save()
    except:
        return render(request, 'cars/car/create.html', {'error_message': 'There was an error saving the car details!'})
    return render(request, 'cars/car/view.html', {'car': car, 'success_message': 'Car has been added!'})


def all_cars(request):
    cars = Car.objects.order_by('id')
    return render(request, 'cars/car/index.html', {'cars': cars})


def view_car(request, id):
    car = get_object_or_404(Car, pk=id)
    return render(request, 'cars/car/view.html', {'car': car})

def edit_car(request, id):
    car = get_object_or_404(Car, pk=id)
    return render(request, 'cars/car/edit.html', {'car': car})


@check_for_empty_fields
def update_car(request, id):
    car = get_object_or_404(Car, pk=id)
    car.name = request.POST['name'] if request.POST['name'] != '' else car.name
    car.model = request.POST['model'] if request.POST['model'] else car.model
    car.colour = request.POST['colour'] if request.POST['colour'] else car.colour
    car.year = request.POST['year'] if request.POST['year'] else car.year
    try:
        car.save()
    except:
        return render(request, 'cars/car/edit.html', {'error_message': 'There was an error updating the car details!', 'car': car})
    return render(request, 'cars/car/view.html', {'car': car, 'success_message': 'Car was updated successfully!'})
