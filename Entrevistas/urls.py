from Entrevistas import views
from django.urls import path

urlpatterns = [
    path('',views.EntrevistaCreate.as_view(), name="EntrevistaCreate"),
    path('Listar/',views.EntrevistaList.as_view(), name="EntrevistaList"),
    path('<pk>/',views.EntrevistaDetail.as_view(), name="EntrevistaDetail"),
    path('editar/<pk>/',views.EntrevistaUpdate.as_view(), name="EntrevistaUpdate"),
    path('borrar/<pk>/',views.EntrevistaDelete.as_view(), name="EntrevistaDelete"),
]
