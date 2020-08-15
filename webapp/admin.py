from django.contrib import admin

# Register your models here.
from webapp.models import Member, Period

admin.site.register(Member)
admin.site.register(Period)
