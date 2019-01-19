from django.shortcuts import render
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
    return render(request, 'cars/index.html', {})


def all_cars(request):
    cars = Car.objects.order_by('id')
    return render(request, 'cars/car/index.html', {'cars': cars})
