from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity

from django.shortcuts import render
from django.http import HttpResponse
from .forms import ActivityForm

def activity_create(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponse("""
            <script>
              const modal = bootstrap.Modal.getInstance(document.getElementById('activitymodal'));
              modal.hide();

              document.body.dispatchEvent(new Event("activityAdded"));
            </script>
            """)

        # ❌ If form invalid → return form WITH errors
        return render(request, "partials/activity_form.html", {"form": form})

    # GET request
    form = ActivityForm()
    return render(request, "partials/activity_form.html", {"form": form})

    
def activity_list(request):
    activities = Activity.objects.all().order_by('-created_at')
    return render(request, "partials/activity_list.html", {
        "activities": activities
    })