from django.shortcuts import render
from .models import courseType,courseStore
from django.shortcuts import get_object_or_404
from .forms import courseTypeForm

# Create your views here.

def all_tut(request):
    courses = courseType.objects.all()
    return render(request, 'tutorial/all_tutorial.html',{'courses': courses})

def detail(request,course_id):
    course = get_object_or_404(courseType, pk=course_id)
    if course is not None:
        return render(request, 'tutorial/detail.html',{'course': course})    

def courseStoreView(request):
    stores = None
    if request.method == 'POST':
        form = courseTypeForm(request.POST)
        if form.is_valid():
            course_type = form.cleaned_data['course_type']
            stores = courseStore.objects.filter(course_types = course_type)
    else:
        form = courseTypeForm()

    return render(request, 'tutorial/course_stores.html', {'stores': stores,'form': form})