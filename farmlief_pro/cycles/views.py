from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Cycle
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

    context = {'cycles' : page_obj}
    return render(request, 'cycle_list.html', context)


def cycle_detail(request):
    return render(request, 'cycle_detail.html')