from django.shortcuts import render
from django.views.generic import ListView
from .models import Clinic

class ClinicList(ListView):
    template_name = 'clinicas/lista_clinicas.html'
    queryset = Clinic.objects.all()

class ClinicSearch(ListView):
    template_name = 'clinicas/buscar_clinicas.html'
    queryset = Clinic.objects.all()