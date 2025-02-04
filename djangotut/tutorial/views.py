from django.shortcuts import render
from .models import courseType

# Create your views here.

def all_tut(request):
    courses = courseType.objects.all()
    return render(request, 'tutorial/all_tutorial.html',{'courses': courses})

