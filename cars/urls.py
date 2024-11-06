from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.urls import path
from .views import CarsListCreateView

urlpatterns = [
    path('', CarsListCreateView.as_view(), name='cars_list_create'),
]