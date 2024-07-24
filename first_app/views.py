from django.shortcuts import render

# Create your views here.
def index(request):
    diction = {'text_1': 'Silly text'}
    return render(request, 'first_app/index.html', context=diction)
