from unicodedata import name
from .views import *
from django.urls import include, path

urlpatterns = [
    path('', products, name='productos'),
    path('ordenes/', order, name='ordenes'),
    path('exito/', success, name='success'),
]
