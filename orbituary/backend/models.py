from django.db import models
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.utils import timezone

class Obituary(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    content = models.TextField(default='Content not provided')
    author = models.CharField(max_length=100, default='Anonymous')
    submission_date = models.DateField(default=timezone.now)
    slug = models.SlugField(unique=True, max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

def add_obituary(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        date_of_death = request.POST.get('date_of_death')
        content = request.POST.get('content')
        author = request.POST.get('author')
        submission_date = request.POST.get('submission_date')

        # Create and save the Obituary object
        new_obituary = Obituary(
            name=name,
            date_of_birth=date_of_birth,
            date_of_death=date_of_death,
            content=content,
            author=author,
            submission_date=submission_date,
            slug=slugify(name)  # Generate a slug from the name
        )
        new_obituary.save()

        # Redirect to a success page or any other page
        return redirect('home')  # Replace with the appropriate URL name

    # If GET request or form is not valid, render the form template
    return render(request, 'frontend/submit_obituary.html')

def home(request):
    obituaries = Obituary.objects.all()
    return render(request, 'frontend/home.html', {'obituaries': obituaries})
