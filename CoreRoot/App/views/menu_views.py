from django.shortcuts import render
from App.models import NuestraPropuesta, PreguntasFrecuentes, QuienesSomos


def propuestas(request):
    propuestas = NuestraPropuesta.objects.all()
    return render(request, "Propuesta/propuesta.html", {"propuestas": propuestas})

def preguntas_frecuentes(request):
    preguntas_frecuentes = PreguntasFrecuentes.objects.all()
    return render(request, "FAQ/preguntas_frecuentes.html", {"preguntas_frecuentes": preguntas_frecuentes})


def quienes_somos(request):
    quienes_somos_info = QuienesSomos.objects.all()
    return render(request, 'QuienesSomos/quienes_somos.html', {'quienes_somos_info': quienes_somos_info})