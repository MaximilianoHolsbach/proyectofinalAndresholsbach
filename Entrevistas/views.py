from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from Entrevistas.models import EntrevistasModel

class EntrevistaList(ListView):
    model = EntrevistasModel
    template_name = "Entrevistas/Entrevistaslist.html"

class EntrevistaDetail(DetailView):
    model = EntrevistasModel
    template_name = "Entrevistas/Entrevistasdetail.html"

class EntrevistaCreate(CreateView):
    model = EntrevistasModel
    success_url = reverse_lazy("EntrevistaList")
    fields = ["Titulo", "Localidad", "Entrevistado", "Anecdota", "Corresponsal"]

class EntrevistaUpdate(UpdateView):
    model = EntrevistasModel
    success_url = reverse_lazy("EntrevistaList")
    fields = ["Titulo", "Localidad", "Entrevistado", "Anecdota", "Corresponsal"]

class EntrevistaDelete(DeleteView):
    model = EntrevistasModel
    success_url = reverse_lazy("EntrevistaList")
# Create your views here.
