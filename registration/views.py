from django.shortcuts import render
from django.http import HttpResponse

from .models import Events

# Create your views here.
def homeView(request):
    eventsList = Events.objects.all()
    context = {}
    context['events'] = eventsList
    return render(request, 'home.html', context)

def registerView(request):
    return render(request, 'register.html')