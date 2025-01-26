from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/dropdowns/', views.get_dropdown_values, name='get_dropdown_values'),
    path('api/filter_standards/', views.filter_standards, name='filter_standards'),
]
