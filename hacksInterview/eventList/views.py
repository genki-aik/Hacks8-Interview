from django.shortcuts import render

from .models import Event

# Create your views here.
def homePage(request):
    # Query the Event

    return render(request, 'eventList/home.html')