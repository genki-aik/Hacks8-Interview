from django.shortcuts import render

# Import the model

# Create your views here.
def homePage(request):
    # Query the Event

    return render(request, 'eventList/home.html')