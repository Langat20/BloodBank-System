from django.contrib import admin

from donor.models import BloodDonate, Donor

# Register your models here.
admin.site.register(BloodDonate)
admin.site.register(Donor)