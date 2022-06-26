from Entrevistas import views
from django.urls import path

urlpatterns = [
    path('',views.Entrevistainicio.as_view(), name="Entrevistainicio"),
    path('entevistaslistas/',views.EntrevistaList.as_view(), name="EntrevistaList"),
    path('crear/',views.EntrevistaCreate.as_view(), name="EntrevistaCreate"),
    path('detalle/<pk>/',views.EntrevistaDetail.as_view(), name="EntrevistaDetail"),
    path('editar/<pk>/',views.EntrevistaUpdate.as_view(), name="EntrevistaUpdate"),
    path('borrar/<pk>/',views.EntrevistaDelete.as_view(), name="EntrevistaDelete"),
    path('entrar/',views.EntrevistaLogin.as_view(), name="EntrevistaLogin"),
    path('salir/',views.EntrevistaLogout.as_view(), name="EntrevistaLogout"),
    path('crearcorresponsal/',views.SignUpView.as_view(), name="EntrevistaSignUpView"),
    path('soy/',views.About.as_view(), name="EntrevistaAbout"),
]

