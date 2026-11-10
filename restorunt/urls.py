from django.urls import path
from .views import *



urlpatterns = [
    path('', add_category, name='home'),
    path('add_cat', add_category, name='add_cat'),
    path('add_dish', add_dish, name='add_dish'),
    path('add_table_number', add_table_number, name='table_number'),
    path('home_page2', home_page2, name='home_pge')
]
