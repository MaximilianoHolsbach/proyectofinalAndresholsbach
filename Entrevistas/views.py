from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from Entrevistas.models import EntrevistasModel
from django.db.models import Q

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Entrevistas/Entrevistaabout.html", {})

class Entrevistainicio(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "Entrevistas/Entrevistainicio.html", {})



class EntrevistaList(ListView):
    model = EntrevistasModel
    template_name = "Entrevistas/Entrevistaslist.html"

class EntrevistaDetail(DetailView):
    model = EntrevistasModel
    template_name = "Entrevistas/Entrevistasdetail.html"

class EntrevistaCreate(LoginRequiredMixin, CreateView):
    model = EntrevistasModel
    success_url = reverse_lazy("EntrevistaList")
    fields = ["Titulo", "Localidad", "Entrevistado", "Anecdota", "Corresponsal","Imagen"]
    def form_valid(self, form):
        form.instance.Corresponsal = self.request.user
        return super().form_valid(form)

class EntrevistaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EntrevistasModel
    success_url = reverse_lazy("EntrevistaList")
    fields = ["Titulo", "Localidad", "Entrevistado", "Anecdota", "Corresponsal"]
    def test_func(self):
        exist = EntrevistasModel.objects.filter(Corresponsal=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False


class EntrevistaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EntrevistasModel
    success_url = reverse_lazy("EntrevistaList")
    def test_func(self):
        exist = EntrevistasModel.objects.filter(Corresponsal=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False


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
