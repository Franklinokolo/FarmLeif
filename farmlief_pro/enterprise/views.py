from django.shortcuts import render

# Create your views here.


# Enterprise view Here
def dashboardView(request):
    return render(request,'dashbaord.html')