# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .serializers import StandardSerializer, MarksheetSerializer
from rest_framework import viewsets
from models import Marksheet, Standard

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "result/index.html")
    else:
        return render(request, "accounts/profile.html")


class MarksheetViewSet(viewsets.ModelViewSet):
    queryset = Marksheet.objects.all()
    serializer_class = MarksheetSerializer


class StandardViewSet(viewsets.ModelViewSet):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer
