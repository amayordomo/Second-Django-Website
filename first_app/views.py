from django.shortcuts import render
from .models import Musician, Album
from first_app import forms_django

# Create your views here.
def index(request):
    diction = {'sample_text': "Sample text"}
    return render(request, 'first_app/index.html', context=diction)

def form(request):
    new_form = forms_django.MusicianForm()

    if request.method == 'POST':
        new_form = forms_django.MusicianForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
        
    
    diction = {'test_form' : new_form, 'heading_1': 'Add New Musician'}
    
    return render(request, 'first_app/form.html', context=diction)