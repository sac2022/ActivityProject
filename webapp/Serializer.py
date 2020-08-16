from rest_framework import serializers

from .models import Member, Period


# creating a Serializer for Serializing the data
class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period  # Specifying the model name
        fields = ['start', 'end']  # fetching the data and linking to fields


# Serializing the data from the model
class MemberSerializer(serializers.ModelSerializer):
    activity_periods = PeriodSerializer(many=True, read_only=True)  # Embedding or appending data from PeriodSerializer

    class Meta:
        model = Member  # Specifying the model name
        fields = ['mem_id', 'real_name', 'tz', 'activity_periods']  # fetching the data and linking to fields
