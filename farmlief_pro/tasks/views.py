from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Task

# Create your views here.
def alltask(request):
    state = request.GET.get('status', 'all')
    view = request.GET.get('view', 'mobile')
    page_number = request.GET.get('page', 1)

    if state == 'all':
        tasks = Task.objects.all().order_by('-created_at')
    else:
        tasks = Task.objects.filter(status = state).order_by('-created_at')
    
    counts_query = Task.objects.values('status').annotate(total=Count('id'))
    status_counts = {item['status']: item['total'] for item in counts_query}
    status_counts['total'] = Task.objects.count()
    
    paginator = Paginator(tasks, 10)
    page_obj = paginator.get_page(page_number)

    context = {"tasks" : page_obj, 'current_state' : state, 'count' : status_counts}

    if request.headers.get("HX-REQUEST") == 'true':
        if view == 'desktop':
            return render(request, 'partials/desktop/tasks_list.html', context)
        return render(request, 'partials/tasks_list.html', context)
    
    return render(request, 'task_list.html', context)