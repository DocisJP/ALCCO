from django.urls import path
from . import views
from .views import DonacionView, NoticiaDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('sections/', views.sections, name='sections'),
    
    # Menu
    path('nuestra_propuesta/', views.propuestas, name='propuesta'),
    path('preguntas_frecuentes/', views.preguntas_frecuentes, name='preguntas_frecuentes'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),

    # Contacto
    path('contacto/', views.contacto, name='contacto'),
    path('success/', views.success, name='success'),
    
    # Noticias
    path('noticias/', views.noticias, name='noticias'),
    path('noticia/<int:pk>/', NoticiaDetailView.as_view(), name='noticia_detail'),
    
    # Donaciones
    path('donaciones/', DonacionView.as_view(), name='donaciones'),
    
    # Eventos
    path('eventos/<int:year>/<int:month>/', views.eventos_views.calendar_view, name='calendar'),
    path('eventos/', views.eventos, name='eventos'),
    path('eventos/detail/<int:event_id>/', views.eventos_views.event_detail, name='event_detail'),
    path('eventos/<int:year>/<int:month>/<int:day>/', views.eventos_views.day_detail, name='day_detail'),


]
