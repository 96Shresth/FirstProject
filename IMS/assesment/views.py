from django.shortcuts import render
from .models import incident
from .seriealizers import ManagementSerializer
from rest_framework import viewsets

class IncidentModelViewset(viewsets.ModelViewSet):
    queryset = incident.objects.all()
    serializer_class = ManagementSerializer
