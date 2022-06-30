from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from desafio.models import Prueba   

# Create your views here.
def vista_desafio(request):
    return HttpResponse('<h1>Mi perro dinamita')

def un_desafio(request):
    template = loader.get_template('index.html')  

    lista_padres = Prueba.objects.all()

    
    render = template.render({'lista_objetos': lista_padres})
    return HttpResponse(render)