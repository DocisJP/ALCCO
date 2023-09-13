from django.contrib import admin
from .models import Section, Banner, Noticia, Eventos, QuienesSomos, PreguntasFrecuentes, NuestraPropuesta

# Register your models here.
admin.site.register(Section)
admin.site.register(Banner)
admin.site.register(Noticia)
admin.site.register(Eventos)
admin.site.register(QuienesSomos)
admin.site.register(PreguntasFrecuentes)
admin.site.register(NuestraPropuesta)

