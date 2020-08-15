from abc import ABC

import pytz
import six
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Member, Period


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        #fields = ('mem_id', 'real_name', 'tz')
        fields = '__all__'


class PeriodSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Period
        fields = '__all__'

