# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countries/', views.country_list, name='country'),
    path('departments/', views.department_list, name='department'),
    path('cities/', views.city_list, name='city'),
]
