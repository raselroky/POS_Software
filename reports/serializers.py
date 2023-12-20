from rest_framework import serializers
from .models import All_Reports

class All_Reports_Serializer(serializers.ModelSerializer):
    class Meta:
        model=All_Reports
        fields=('__all__')
