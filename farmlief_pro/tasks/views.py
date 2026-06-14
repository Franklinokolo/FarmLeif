from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Task

# Create your views here.
def alltask(request):
    tasks = Task.objects.all().order_by('status')
    page_number  = request.GET.get('page')
    paginator = Paginator(tasks, 1)
    page_obj = paginator.get_page(page_number)
    
    if request.headers.get("HX-REQUEST"):
        state = request.GET.get('status', '')
        tasks = Task.objects.filter(status = state).order_by('-created_at')
        page_number  = request.GET.get('page')
        paginator = Paginator(tasks, 1)
        page_obj = paginator.get_page(page_number)
        return render(request, {'tasks' : page_obj})

    return render(request, 'task_list.html', {'tasks': page_obj} )
