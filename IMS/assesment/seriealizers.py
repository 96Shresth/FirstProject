from dataclasses import fields
from pyexpat import model
from executing import Source
from rest_framework import serializers
from django.contrib.auth.models import User

from assesment.models import incident


class ManagementSerializer(serializers.ModelSerializer):
   
    reporter_name = serializers.SerializerMethodField()
   
    class Meta:
        model=incident
        exclude = ['id']
        
    def get_reporter_name(self,obj):
        return obj.reporter_name.username
