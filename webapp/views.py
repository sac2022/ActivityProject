from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_list_or_404
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter
from .models import Member, Period
from django.contrib.auth.models import User, Group

from .Serializer import ItemSerializer, PeriodSerializer

import json


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # parsing the data and arranging by the members id
    queryset = Member.objects.all().order_by("mem_id")
    serializer_class = ItemSerializer

    def get_queryset(self):
        return self.queryset

    def get_serializer(self, *args, **kwargs):
        return self.queryset, self.serializer_class


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer

    def get_queryset(self):
        return self.queryset

    def get_serializer(self, *args, **kwargs):
        return self.queryset, self.serializer_class