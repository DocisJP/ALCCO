from django.shortcuts import render
from App.models import Noticia
from django.views.generic.detail import DetailView

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'Noticias/noticia_detail.html'

def noticias (request):
    noticias = Noticia.objects.all().order_by('-fecha')
    return render(request, "Noticias/noticias.html", {"noticias":noticias})
