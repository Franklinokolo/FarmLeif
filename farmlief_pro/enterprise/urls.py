from django.urls import path
from . import views

app_name = 'enterprise'

urlpatterns = [
    path('login/', views.loginView, name = 'login'),
    path('dashboard/', views.dashboardView, name = 'dashboard'),
    path('metrics/', views.metrics_partial, name='metrics_partial'),
  
]