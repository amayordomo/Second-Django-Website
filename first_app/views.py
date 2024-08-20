from django.shortcuts import render
from .models import Musician, Album

# Create your views here.
def index(request):
    musician_list = Musician.objects.order_by('first_name')

    diction = {'text_1': 'This is a list of musicians from our database', 'musician': musician_list}
    return render(request, 'first_app/index.html', context=diction)

def form(request):
    diction = {}
    return render(request, 'first_app/form.html', context=diction)