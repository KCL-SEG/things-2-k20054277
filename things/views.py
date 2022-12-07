from django.shortcuts import render
from .forms import ThingForm

def home(request):
    template_name = 'home.html'
    form = ThingForm()

    return render(request, 'home.html', {'form': form})
