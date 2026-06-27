from django.urls import path
from .import views

app_name = 'cycle'

urlpatterns = [
    path('list/', views.cycle_list, name='list' ),
    path('detail/<int:cycle>', views.cycle_detail, name='detail' ),

]
