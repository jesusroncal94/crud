from django.urls import path
from . import views

urlpatterns = [
    path('$', views.home, name="index"),
    path('crear_mascota/', views.crearMascota, name="crear_Mascota"),
]