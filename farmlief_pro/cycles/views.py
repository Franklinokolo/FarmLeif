from django.shortcuts import render

# Create your views here.

def cycle_list(request):
    return render(request, 'cycle_list.html')


def cycle_detail(request):
    return render(request, 'cycle_detail.html')