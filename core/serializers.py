from rest_framework import serializers
from .models import *


class CasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cases
        fields = '__all__'