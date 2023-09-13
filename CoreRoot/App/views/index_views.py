from django.shortcuts import render, redirect
from App.models import Section, Banner


def index(request):
    sections = Section.objects.all()
    banner = Banner.objects.first()
    return render(request, 'Index/index.html', {'sections': sections, 'banner': banner})

def sections(request):
    sections = Section.objects.all()
    return render(request, "sections.html", {"sections": sections})

