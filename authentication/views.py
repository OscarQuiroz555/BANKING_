from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Country
from .forms import CountryForm

def country_list(request):
    search = request.GET.get('search', '')
    countries = Country.objects.filter(name__icontains=search).order_by('name')
    
    paginator = Paginator(countries, 10)  # 10 por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'banking_app/country_list.html', {'countries': page_obj, 'search': search})

def country_create(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'País creado correctamente.')
            return redirect('banking_app:country_list')
    else:
        form = CountryForm()
    return render(request, 'banking_app/country_form.html', {'form': form, 'country': None})

def country_edit(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            messages.success(request, 'País actualizado correctamente.')
            return redirect('banking_app:country_list')
    else:
        form = CountryForm(instance=country)
    return render(request, 'banking_app/country_form.html', {'form': form, 'country': country})

def country_delete(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        country.delete()
        messages.success(request, 'País eliminado correctamente.')
        return redirect('banking_app:country_list')
    return render(request, 'banking_app/country_delete.html', {'country': country})
