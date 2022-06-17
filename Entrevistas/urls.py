from Entrevistas import views
from django.urls import path

urlpatterns = [
    path('crear/',views.EntrevistaCreate.as_view(), name="EntrevistaCreate"),
    path('',views.EntrevistaList.as_view(), name="EntrevistaList"),
    path('detalle/<pk>/',views.EntrevistaDetail.as_view(), name="EntrevistaDetail"),
    path('editar/<pk>/',views.EntrevistaUpdate.as_view(), name="EntrevistaUpdate"),
    path('borrar/<pk>/',views.EntrevistaDelete.as_view(), name="EntrevistaDelete"),
    path('entrar/',views.EntrevistaLogin.as_view(), name="EntrevistaLogin"),
    path('salir/',views.EntrevistaLogin.as_view(), name="EntrevistaLogout"),
    path('crearperfil/',views.SignUpView.as_view(), name="EntrevistaSignUpView"),
]

