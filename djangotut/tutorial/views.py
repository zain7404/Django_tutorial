from django.shortcuts import render
from .models import courseType
from django.shortcuts import get_object_or_404

# Create your views here.

def all_tut(request):
    courses = courseType.objects.all()
    return render(request, 'tutorial/all_tutorial.html',{'courses': courses})

def detail(request,course_id):
    course = get_object_or_404(courseType, pk=course_id)
    if course is not None:
        return render(request, 'tutorial/detail.html',{'course': course})    
