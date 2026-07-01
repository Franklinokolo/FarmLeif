from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Count
import json
from .models import Cycle
from activities.models import Activity
from .forms import cycleForm
# Create your views here.

def cycle_list(request):
    status = request.GET.get('status', 'all')
    if status == 'all':
        cycles = Cycle.objects.all().order_by('-created_at')
    else:
        cycles = Cycle.objects.filter(status = status).order_by('-created_at')
    
    page_number = request.GET.get('page',1)
    paginator = Paginator(cycles, 10)
    page_obj = paginator.get_page(page_number)

    counts_query = Cycle.objects.values('status').annotate(total=Count('id'))
    status_counts = {item['status']: item['total'] for item in counts_query}
    status_counts['total'] = Cycle.objects.count()

    context = {'cycles' : page_obj, 'count' : status_counts}
    return render(request, 'cycle_list.html', context)


def cycle_detail(request, cycle):
    detail = get_object_or_404(Cycle, id = cycle)
    activities = Activity.objects.filter(cycle = cycle)[:5]
    context = {
        "cycle" : detail,
        'activities' : activities
    }
    return render(request, 'cycle_detail.html', context)


def cycleCreate(request):
   
    if request.method == 'POST':
        form =  cycleForm(request.POST)
        if form.is_valid():
            form.save()
            # Create an empty success response
            response = HttpResponse(status=204) 
                
            # Send triggers back to HTMX to execute JavaScript on the frontend
            response['HX-Trigger'] = json.dumps({
                    "activityAdded": "", 
                    "showToast": "Batch created successfully!"
                })
            return response
        else:
            print(form.errors)
    else:
        form = cycleForm()
    
    return render(request, 'modals/cycle_create.html', {'form': form})