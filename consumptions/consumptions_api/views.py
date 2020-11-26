from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from .serializers import ConsumptionSerializer
from .models import Consumptions

# Create your views here.
def main(request):
    return HttpResponse("Testing")

class ConsumptionsViewList(generics.ListCreateAPIView):
    queryset = Consumptions.objects.all()
    serializer_class = ConsumptionSerializer

class ConsumptionsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consumptions.objects.all()
    serializer_class = ConsumptionSerializer