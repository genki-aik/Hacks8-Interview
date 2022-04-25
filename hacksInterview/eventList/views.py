from django.shortcuts import render

from .models import Event

# Create your views here.
def homePage(request):
    # Query the Event
    events = Event.objects.all()

    context = {
        'events': events
    }

    return render(request, 'eventList/home.html', context)