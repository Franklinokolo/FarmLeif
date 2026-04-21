from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncWeek, TruncYear

def get_monthly_metrics(transactions, current_date, last_date):

    def month_data(tx, date):
        return tx.filter(
            date__month=date.month,
            date__year=date.year
        )

    current = month_data(transactions, current_date)
    last = month_data(transactions, last_date)

    def totals(qs):
        income = qs.filter(transaction_type='income').aggregate(total=Sum('amount'))['total'] or 0
        expense = qs.filter(transaction_type='expense').aggregate(total=Sum('amount'))['total'] or 0
        return income, expense, income - expense

    c_income, c_expense, c_profit = totals(current)
    l_income, l_expense, l_profit = totals(last)

    def pct_change(current, last):
        if last > 0:
            return ((current - last) / last) * 100
        elif current > 0:
            return 100
        return 0

    return {
        "total_income": c_income + l_income,  # optional global (or adjust)
        "total_expenses": c_expense + l_expense,
        "total_profit": c_profit + l_profit,

        "income_change": pct_change(c_income, l_income),
        "expense_change": pct_change(c_expense, l_expense),
        "profit_change": pct_change(c_profit, l_profit),

        "current_income": c_income,
        "current_expense": c_expense,
    }





def get_chart_data(transactions, period="monthly"):

    if period == "weekly":
        grouped = TruncWeek('date')
    elif period == "yearly":
        grouped = TruncYear('date')
    else:
        grouped = TruncMonth('date')

    data = (
        transactions
        .annotate(period_key=grouped)
        .values('period_key', 'transaction_type')
        .annotate(total=Sum('amount'))
        .order_by('period_key')
    )

    # get unique sorted labels
    labels = sorted(set(x['period_key'] for x in data))

    income = []
    expense = []

    for l in labels:
        income.append(
            sum(x['total'] for x in data
                if x['period_key'] == l and x['transaction_type'] == 'income')
        )

        expense.append(
            sum(x['total'] for x in data
                if x['period_key'] == l and x['transaction_type'] == 'expense')
        )

    return {
        "labels": [l.strftime("%b %Y") for l in labels],
        "income": income,
        "expense": expense
    }