from django.db import models
import pytz
from rest_framework import serializers
from timezone_field import TimeZoneField

# Create your models here.
import pytz
from django.utils import timezone


class Member(models.Model):
    mem_id = models.CharField(max_length=12)
    real_name = models.CharField(max_length=60)
    tz = models.CharField(max_length=60)

    def __str__(self):
        return self.real_name


class Period(models.Model):
    member = models.ForeignKey(Member,related_name="activity", on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __unicode__(self):
        return self.member
