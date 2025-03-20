from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/dropdowns/', views.get_dropdown_values, name='get_dropdown_values'),
    path('api/filter_standards/', views.filter_standards, name='filter_standards'),
    path('api/filter-attributes/', views.filter_attributes, name='filter_attributes'),
    path('api/get-scopes-categories/', views.get_scopes_categories, name='get_scopes_categories'),

]
