from django.conf import settings
from django.urls import path
from Comentar import views

urlpatterns = [
    path('comentarlist/',views.ComentarList.as_view(), name="ComentarList"),
    path('comentar/<pk>/',views.ComentarCreate.as_view(), name="ComentarCreate"),
    path('comentariosdetalles/<pk>/',views.ComentarDetail.as_view(), name="ComentarDetail"),
    path('comentariosdelete/<pk>/',views.ComentarDelete.as_view(), name="ComentarDelete"), 
]