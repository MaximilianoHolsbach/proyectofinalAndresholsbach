from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'Corresponsales/Corresponsales_crear_cuenta_form.html'
  success_url = reverse_lazy('EntrevistaLogin')
  form_class = UserCreationForm
  success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"

class CorresponsalesProfile(DetailView):
    model = User
    template_name = "Corresponsales/Corresponsalesdetail.html"


class CorresponsalesUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "Corresponsales/user_form.html"
    fields = ["username", "email", "first_name", "last_name"]
    def get_success_url(self):
        return reverse_lazy("CorresponsalesProfile", kwargs={"pk": self.request.user.id})


# Create your views here.
