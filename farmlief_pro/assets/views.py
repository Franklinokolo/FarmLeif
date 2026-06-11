from django.shortcuts import render

# Create your views here.
def assets_list(request):
    return render(request, 'assets_list.html')


def assets_detail(request):
    return render(request, 'assets_detail.html')