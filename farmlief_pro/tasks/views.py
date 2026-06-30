from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Task
from .forms import taskForm
import time

def alltask(request):
    state = request.GET.get('status', 'all')
    search = request.GET.get('searchTask')
    view = request.GET.get('view', 'mobile')
    page_number = request.GET.get('page', 1)

    # 1. Handle Search Filter Globally
    if search:
        tasks = Task.objects.filter(title__icontains=search).order_by('-created_at')
    else:
        # 2. Handle Status State Filters using Custom Manager
        if state == 'pending':
            tasks = Task.objects.pending().order_by('-created_at')
        elif state == 'overdue':
            tasks = Task.objects.overdue().order_by('-created_at')
        elif state == 'completed':
            tasks = Task.objects.filter(is_complete=True).order_by('-created_at')
        else:  # 'all'
            tasks = Task.objects.all().order_by('-created_at')
    
    # 3. Calculate Status Counts Safely without the 'status' database field
    status_counts = {
        'total': Task.objects.count(),
        'pending': Task.objects.pending().count(),
        'overdue': Task.objects.overdue().count(),
        'completed': Task.objects.filter(is_complete=True).count(),
    }
    
    # 4. Pagination
    paginator = Paginator(tasks, 3)
    page_obj = paginator.get_page(page_number)

    context = {
        "tasks": page_obj, 
        'current_state': state, 
        'count': status_counts
    }

    # 5. HTMX Request Layout Splitting
    if request.headers.get("HX-REQUEST") == 'true':
        if view == 'desktop':
            return render(request, 'partials/desktop/tasks_list.html', context)
        return render(request, 'partials/tasks_list.html', context)
    
    return render(request, 'task_list.html', context)

def TaskCreate(request):
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("""
            <script>
              const modal = bootstrap.Modal.getInstance(document.getElementById('modalform'));
              modal.hide();

              document.body.dispatchEvent(new Event("activityAdded"));
            </script>
            """)
    else:
    
        form = taskForm()
    return render(request, 'modals/task_create.html', {'form' : form})