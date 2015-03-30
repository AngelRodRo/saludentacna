from django.shortcuts import render

from django.db.models import Q
from django.views.generic import ListView
from .models import Clinic

class ClinicList(ListView):
    template_name = 'clinicas/lista_clinicas.html'
    queryset = Clinic.objects.all()

class ClinicSearch(ListView):
    template_name = 'clinicas/resultado.html'
    model = Clinic

    def get(self,request):
        if 'q' in request.GET and request.GET['q']:
            q = request.GET['q']
            clinics = Clinic.objects.filter(nombre=q)
            return render(request,'clinicas/resultado.html',{'object_list':clinics,'query':q})
        else:
            return render(request,'clinicas/resultado.html',{'object_list':'','query':''})