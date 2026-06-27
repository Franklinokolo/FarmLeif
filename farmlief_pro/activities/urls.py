from django.urls import path
from . import views

app_name = "activity"

urlpatterns = [
    path('create/', views.activity_create, name='create'),
    path('list/', views.activity_list, name='list'),
    path('search/', views.searchActivity, name='search'),
    path('detail/', views.activity_detail, name='detail')
]