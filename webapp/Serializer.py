from rest_framework import serializers
from .models import Member, Period


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ['start', 'end']


# Serializing the data from the model
class ItemSerializer(serializers.ModelSerializer):
    activity_periods = PeriodSerializer(many=True, read_only=True)

    class Meta:
        model = Member
        fields = ['mem_id', 'real_name', 'tz', 'activity_periods']
