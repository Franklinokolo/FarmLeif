from django.urls import path
from . import views

app_name = 'enterprise'

urlpatterns = [
    path('login/', views.loginView, name = 'login'),
    path('logout/', views.logoutView, name= 'logout'),
    path('', views.dashboardView, name = 'dashboard'),
    path('metrics/', views.metrics_partial, name='metrics_partial'),

    # enterprise url
    path('enterprises/', views.enterpriseList, name='list')
  
]