from django.shortcuts import render
from rest_framework import viewsets
from .models import Hudud, Tashkilot, Bino
from .serializers import HududSerializer, TashkilotSerializer, BinoSerializer
# Create your views here.

class HududApiViewSet(viewsets.ModelViewSet):
    queryset = Hudud.objects.all()
    serializer_class = HududSerializer


class TashkilotApiViewSet(viewsets.ModelViewSet):
    queryset = Tashkilot.objects.all()
    serializer_class = TashkilotSerializer

class BinoApiViewSet(viewsets.ModelViewSet):
    queryset = Bino.objects.all()
    serializer_class = BinoSerializer