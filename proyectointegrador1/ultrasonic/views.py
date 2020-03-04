from django.shortcuts import render
from rest_framework import viewsets
from .models import Ultrasonic
from .serializer import UltrasonicSerializer

# Create your views here.

class UltrasonicViewSet(viewsets.ModelViewSet):
    queryset = Ultrasonic.objects.all().order_by('-created')
    serializer_class = UltrasonicSerializer