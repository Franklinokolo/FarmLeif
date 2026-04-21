from django.urls import path
from . import views

app_name = "activities"

urlpatterns = [
    path('create/', views.activity_create, name='activity_create'),
    path('list/', views.activity_list, name='activity_list'),
]