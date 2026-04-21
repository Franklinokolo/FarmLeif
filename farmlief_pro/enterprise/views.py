from django.shortcuts import render
from django.db.models import Sum

# Create your views here.
from activities.models import Activity
from cycles.models import Cycle
from transactions.models import Transaction
from .models import Enterprise, Farmer

from django.utils import timezone
from datetime import timedelta
from transactions.services import get_monthly_metrics, get_chart_data

# login view for farmers to login and manage their enterprise
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def loginView(request):
    if request.user.is_authenticated:
        return redirect('enterprise:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('enterprise:dashboard')
        else:
            return render(request, 'business/login.html', {'error': 'Invalid credentials'})

    return render(request, 'business/login.html')


def logoutView(request):
    logout(request)
    return redirect('enterprise:login')


# Enterprise view Here
@login_required
def dashboardView(request):
    user = request.user
    enterprise = Enterprise.objects.filter(farmer=user)
    current_enterprise = enterprise.first()

    recent_activities = Activity.objects.filter(enterprise=current_enterprise).order_by('-created_at')[:5]
    cycles = Cycle.objects.filter(enterprise=current_enterprise)

    period = request.GET.get("chart", "monthly")
    
    transactions = Transaction.objects.filter(enterprise=current_enterprise)
    chart_data = get_chart_data(transactions, period)

    context = {
        "chart_labels": chart_data["labels"],
        "chart_income": chart_data["income"],
        "chart_expense": chart_data["expense"],
        "chart_mode": period,
        'enterprise': current_enterprise,
        'recent_activities': recent_activities,
        'cycles': cycles,
    }

    return render(request,'dashboard.html', context)




@login_required
def metrics_partial(request):
    enterprise = Enterprise.objects.filter(farmer=request.user).first()
    transactions = Transaction.objects.filter(enterprise=enterprise)

    today = timezone.now()
    last_month = today.replace(day=1) - timedelta(days=1)

    data = get_monthly_metrics(transactions, today, last_month)

    return render(request, "partials/metrics.html", {
        "total_income": data["current_income"],
        "total_expenses": data["current_expense"],
        "total_profit": data["total_profit"],

        "income_change": round(data["income_change"], 1),
        "expense_change": round(data["expense_change"], 1),
        "profit_change": round(data["profit_change"], 1),
    })