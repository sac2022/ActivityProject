from django.db import models


# Create your models here.

# creating two models for the user and activity
class Member(models.Model):
    mem_id = models.CharField(max_length=12)
    real_name = models.CharField(max_length=60)
    tz = models.CharField(max_length=60)

    # name of the field in admin page
    def __str__(self):
        return self.real_name


class Period(models.Model):
    # referring to the Member Class
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __unicode__(self):
        return self.member
