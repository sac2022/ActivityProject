# Create your views here.
from rest_framework import viewsets, permissions

from .Serializer import MemberSerializer, PeriodSerializer
from .models import Member, Period


# Serializers define the API representation.
class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed
    """
    # parsing the data and arranging by the members id
    queryset = Member.objects.all().order_by("mem_id")  # Builds on model,database and is Iterable for objects;
    # objects are been arranged by there member id
    serializer_class = MemberSerializer  # calling the serialize data
    permission_classes = [permissions.IsAuthenticated]  # Provides Authentication for the API


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()  # Builds on model,database and is Iterable for objects;
    # objects are been arranged by there member id
    serializer_class = PeriodSerializer
    permission_classes = [permissions.IsAuthenticated]
