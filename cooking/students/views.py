from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    return render (request, 'students/home.html', {

    })

def about(request):
    return render (request, 'students/about.html', {
        'students': Student.objects.all()
    })