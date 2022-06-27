from django.urls import path
from .views import vista_desafio, un_desafio

urlpatterns = [
    path('',vista_desafio),
    path('mi-template/',un_desafio),
]