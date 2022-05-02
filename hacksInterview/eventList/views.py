from django.shortcuts import render
from eventList.models import Event

# Import the model

# Create your views here.
def homePage(request):
    # Query the Event
    event_qs = Event.objects.all()
    return render(request, 'eventList/home.html', context = {
        'events': event_qs
    })