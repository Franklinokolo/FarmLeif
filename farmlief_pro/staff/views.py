from django.shortcuts import render

# Create your views here.
def staff_view(request):
    return render(request, "staff.html")


def settings_view(request):
    return render(request, 'settings.html')