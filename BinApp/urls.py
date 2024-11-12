# urls.py
from django.urls import path
from .views import modify_scripts

urlpatterns = [
    path('BinForm/', modify_scripts, name='BinForm'),
    # Add other URL patterns as needed
]
