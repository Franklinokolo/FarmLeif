from django.urls import path
from . import views

app_name = 'staff'
urlpatterns = [
    path('list/', views.staff_view,name='list' ),
    path('settings/', views.settings_view, name='setting')
]
