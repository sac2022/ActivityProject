from abc import ABC

import pytz
import six
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Member, Period


class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'

# Serializing the data from the model
class ItemSerializer(serializers.HyperlinkedModelSerializer):
    activity_periods = PeriodSerializer(many=True, read_only=True)

    class Meta:
        model = Member  # model name
        # fields = ('mem_id', 'real_name', 'tz')
        fields = ['mem_id', 'real_name', 'tz', 'activity_periods']



