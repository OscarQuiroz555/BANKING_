# views.py
from django.shortcuts import render
from .models import Country, Department, City

# Página de inicio
def index(request):
    return render(request, 'index.html')  # Aquí puedes crear un archivo index.html en templates

# Listado de países
def country_list(request):
    countries = Country.objects.all()
    return render(request, 'countries.html', {'countries': countries})

# Listado de departamentos
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})

# Listado de ciudades
def city_list(request):
    cities = City.objects.all()
    return render(request, 'cities.html', {'cities': cities})
