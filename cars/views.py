from django.shortcuts import render, redirect

from .models import Car
from .forms import CarForm

def cars_view(request):

    cars = Car.objects.all()
        
    model = request.GET.get('model')
    
    if model:
        cars = cars.filter(model__icontains=model)

    return render(request, 'cars/cars.html', {'carros':cars, 'model':model})

def new_car_view(request):

    new_car_form = CarForm()

    return render(request, 'cars/new_cars.html', {'new_car_form': new_car_form})