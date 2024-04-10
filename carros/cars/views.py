from django.shortcuts import render, redirect

from .models import Car

def cars_view(request):

    cars = Car.objects.all()
    
    model = request.GET.get('model')
    color = request.GET.get('color')
    
    if model:
        cars = cars.filter(model__icontains=model)
    if color:
        cars = cars.filter(color__name__icontains=color)    

    return render(request, 'cars/cars.html', {'carros':cars})