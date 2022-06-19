from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from Comentar.models import ComentarModel
from Entrevistas.models import EntrevistasModel


class ComentarList(ListView):
    model = ComentarModel
    template_name = "Comentar/Comentarlist.html"

class ComentarCreate(CreateView):
    model = ComentarModel
    success_url = reverse_lazy("ComentarList")
    fields = ["Titulo", "Nombre", "Comentario", "Email"]

class ComentarDetail(DetailView):
    model = ComentarModel
    template_name = "Comentar/Comentardetalle.html"

class ComentarDelete(LoginRequiredMixin, DeleteView):
    model = ComentarModel
    success_url = reverse_lazy("ComentarList")


# Create your views here.
