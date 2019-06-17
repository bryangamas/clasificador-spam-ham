from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entrenar', views.entrenar, name='entrenar'),
    path('formulario', views.formulario, name='formulario')
]