from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Obituary
def home(request):
    return render(request, 'frontend/home.html')

def display_obituary(request):
    obituary = Obituary.objects.all()
    return render(request, 'frontend/home.html', {'obituary': obituary})

def add_obituary(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        date_of_death = request.POST.get('date_of_death')
        content = request.POST.get('content')
        author = request.POST.get('author')
        submission_date = request.POST.get('submission_date')
        slug = request.POST.get('slug')

        # Create and save the Obituary object
        obituary = Obituary(
            name=name,
            date_of_birth=date_of_birth,
            date_of_death=date_of_death,
            content=content,
            author=author,
            submission_date=submission_date,
            slug=slug # Assuming you want to generate a slug from the name
        )
        obituary.save()

        # Redirect to a success page or any other page
        return redirect('home')  # Replace with the appropriate URL name

    # If GET request or form is not valid, render the form template
    return render(request, 'frontend/submit_obituary.html')