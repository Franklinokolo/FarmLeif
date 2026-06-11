from django.urls import path
from .import views
app_name = 'assets'

urlpatterns = [
    path('list/', views.assets_list, name='list'),
    path('detail/', views.assets_detail, name='detail')
]
