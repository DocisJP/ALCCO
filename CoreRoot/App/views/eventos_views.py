from django.shortcuts import render, get_object_or_404
from App.models import Eventos
import calendar
from django.utils import timezone



def eventos(request):
    eventos_list = Eventos.objects.order_by('-date', '-time')
    return render(request, 'eventos.html', {'eventos_list': eventos_list})


def calendar_view(request, year=None, month=None):
    now = timezone.now()
    
    if year is None:
        year = now.year
        
    if month is None:
        month = now.month

    month_calendar = calendar.monthcalendar(year, month)
    events = Eventos.objects.filter(date__year=year, date__month=month)

    event_dict = {}
    for event in events:
        event_dict[event.date.day] = event

    return render(request, 'Eventos/calendar.html', {'calendar': month_calendar, 'events': event_dict, 'year': year, 'month': month})

def event_detail(request, event_id):
    event = get_object_or_404(Eventos, id=event_id)
    same_day_events = Eventos.objects.filter(date=event.date)
    return render(request, 'Eventos/event_detail.html', {'events': same_day_events})

def day_detail(request, year, month, day):
    events = Eventos.objects.filter(date__year=year, date__month=month, date__day=day)
    return render(request, 'Eventos/day_detail.html', {'events': events, 'day': day, 'month': month, 'year': year})
