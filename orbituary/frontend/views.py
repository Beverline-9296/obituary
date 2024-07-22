from django.shortcuts import render, redirect
from backend.models import Obituary
from backend.forms import ObituaryForm

def add_obituary(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ObituaryForm()

    return render(request, 'frontend/submit_obituary.html', {'form': form})

def home(request):
    obituaries = Obituary.objects.all()
    return render(request, 'frontend/home.html', {'obituaries': obituaries})
