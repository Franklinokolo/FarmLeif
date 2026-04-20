from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def activity_create(request):
    if request.method == "POST":
        # normally you'd save to DB here

        return HttpResponse("""
        <script>
          var modal = bootstrap.Modal.getInstance(document.getElementById('activitymodal'));
          modal.hide();
          location.reload();
        </script>
        """)

    return render(request, "partials/activity_form.html")