from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Activity
from django.db.models import Q

from .forms import ActivityForm

def activity_create(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)

        if form.is_valid():
            activity = form.save(commit=False)
            activity.enterprise = request.user.enterprises.first()
            activity.save()

            return HttpResponse("""
            <script>
              const modal = bootstrap.Modal.getInstance(document.getElementById('modalform'));
              modal.hide();

              document.body.dispatchEvent(new Event("activityAdded"));
            </script>
            """)

        # If form invalid → return form WITH errors
        return render(request, "modals/activity_create.html", {"form": form})

    # GET request
    form = ActivityForm()
    return render(request, "modals/activity_create.html", {"form": form})

    
def activity_list(request):
    activities = Activity.objects.all().order_by('-created_at')
    total_activity = len(activities)
    pending  = activities.filter(activity_type = 'pending')
    paginator = Paginator(activities, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if request.headers.get("HX-Request"):
        return render(request, 'partials/activity_list.html', {'page_obj': page_obj})
    
    

    
    return render(request, "activities_list.html", {
         'page_obj' : page_obj,
         'total_activity': total_activity,
         'pending_activity' : pending
    })


def searchActivity(request):

    activities = Activity.objects.all()

    if request.method == "POST":

        date = request.POST.get("date")
        batch = request.POST.get("batch")

        if date:
            activities = activities.filter(activity_date=date)

        # if batch:
        #     activities = activities.filter(cycle = batch)

    else:
        search = request.GET.get("search")

        if search:
            activities = activities.filter(
                title__icontains=search
            )

    activities = activities.order_by("-created_at")

    paginator = Paginator(activities, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "partials/activity_list.html",
        {"page_obj": page_obj},
    ) 


def activity_detail(request):
    return render(request, 'activity_detail.html')