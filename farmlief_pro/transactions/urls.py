from django.urls import path
from .import views
app_name = 'transactions'

urlpatterns = [
    path('list/', views.transactions_view, name = 'list'),
    path('create/', views.create_transaction, name='create_transaction'),
]