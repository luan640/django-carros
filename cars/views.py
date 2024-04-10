from django.shortcuts import render, redirect

from .models import Car

def cars_view(request):

    cars = Car.objects.all()
        
    model = request.GET.get('model')
    
    if model:
        cars = cars.filter(model__icontains=model)

    return render(request, 'cars/cars.html', {'carros':cars, 'model':model})

def new_car(request):

    return 'Novo carro'