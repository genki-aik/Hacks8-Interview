from django.shortcuts import render

# Import the model
from eventList import models

# Create your views here.
def homePage(request):
    # Query the Event
    event = models.Event.objects.all()
    eventQuery = {'events': event}

    return render(request, 'eventList/home.html', eventQuery)