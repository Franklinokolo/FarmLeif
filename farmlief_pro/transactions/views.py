from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import TransactionForm
from enterprise.models import Enterprise

@login_required
def create_transaction(request):
    enterprise = Enterprise.objects.filter(farmer=request.user).first()

    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.enterprise = enterprise
            transaction.save()

            response = HttpResponse("")
            response["HX-Trigger"] = "transactionAdded"
            return response

        # 🔥 IMPORTANT: return errors
        return render(request, "partials/tansaction_create_form.html", {"form": form})

    else:
        form = TransactionForm()

    return render(request, "partials/tansaction_create_form.html", {"form": form})