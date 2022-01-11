
from django.urls import path, include
from . import  views

urlpatterns = [
    path('', views.stockPicker, name='stockPicker'),
    path('stockticker/', views.stockTicker, name='stockTicker'),
]
