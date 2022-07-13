from dataclasses import fields
from rest_framework import serializers
from .models import Donor,BloodDonate

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ('user', 'profile_pic','bloodgroup','address', 'mobile')


class BloodDonateSerializer(serializers.ModelSerializer):
    class Meta:
        model=BloodDonate
        fields=('donor','disease','age','bloodgroup','unit','status','date')