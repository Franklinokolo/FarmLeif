from django.shortcuts import render

# Create your views here.
def enterprise_dashboard(request):
    return render(request, "dashbaord.html")