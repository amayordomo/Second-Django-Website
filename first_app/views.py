from django.shortcuts import render
from .models import Musician, Album
from first_app import forms_django

# Create your views here.
def index(request):
    musician_list = Musician.objects.order_by('first_name')

    diction = {'text_1': 'This is a list of musicians from our database', 'musician': musician_list}
    return render(request, 'first_app/index.html', context=diction)

def form(request):
    new_form = forms_django.user_form()
    diction = {'test_form': new_form, 'heading_1': "This is from Django form library"}

    if request.method == "POST":
        new_form = forms_django.user_form(request.POST)

        if new_form.is_valid():
            user_name = new_form.cleaned_data['user_name']
            user_dob = new_form.cleaned_data['user_dob']
            user_email = new_form.cleaned_data['user_email']

            diction.update({'user_name' : user_name})
            diction.update({'user_dob' : user_dob})
            diction.update({'user_email' : user_email})
            diction.update({'form_submitted' : "Yes"})

    return render(request, 'first_app/form.html', context=diction)