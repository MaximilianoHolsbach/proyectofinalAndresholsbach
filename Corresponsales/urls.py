from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Corresponsales import views

urlpatterns = [
    path('crear',views.SignUpView.as_view(), name="CorresponsalesSignUpView"),
    path('perfiles/<pk>/',views.CorresponsalesProfile.as_view(), name="CorresponsalesProfile"), 
    path('editarperfiles/<pk>/',views.CorresponsalesUpdate.as_view(), name="CorresponsalesUpdate"), 
]