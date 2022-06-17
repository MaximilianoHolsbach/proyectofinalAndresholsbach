from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from Entrevistas.models import EntrevistasModel

class About(View):

    def get(self, request, *args, **kwargs):
        return render(request, "Entrevistas/Entrevistaabout.html", {})


class EntrevistaList(ListView):
    model = EntrevistasModel
    template_name = "Entrevistas/Entrevistaslist.html"

class EntrevistaDetail(DetailView):
    model = EntrevistasModel
    template_name = "Entrevistas/Entrevistasdetail.html"

class EntrevistaCreate(LoginRequiredMixin, CreateView):
    model = EntrevistasModel
    success_url = reverse_lazy("EntrevistaList")
    fields = ["Titulo", "Localidad", "Entrevistado", "Anecdota", "Corresponsal"]

class EntrevistaUpdate(LoginRequiredMixin, UpdateView):
    model = EntrevistasModel
    success_url = reverse_lazy("EntrevistaList")
    fields = ["Titulo", "Localidad", "Entrevistado", "Anecdota", "Corresponsal"]

class EntrevistaDelete(LoginRequiredMixin, DeleteView):
    model = EntrevistasModel
    success_url = reverse_lazy("EntrevistaList")

class EntrevistaLogin(LoginView):
    template_name = 'Entrevistas/Entrevistaslogin.html'
    next_page = reverse_lazy("EntrevistaList")


class EntrevistaLogout(LogoutView):
    template_name = 'Entrevistas/Entrevistaslogout.html'

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'Entrevistas/Entrevistas_crear_cuenta.html'
  success_url = reverse_lazy('EntrevistaLogin')
  form_class = UserCreationForm
  success_message = "Tu perfil de corresponsal a sido creado satisfactoriamente."
# Create your views here.
