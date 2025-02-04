from django.shortcuts import render

# Create your views here.

def all_tut(request):
    return render(request, 'tutorial/all_tutorial.html')

