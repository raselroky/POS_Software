from rest_framework import serializers
from .models import Stock_Transfer

class Stock_Transfer_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Stock_Transfer
        fields=('__all__')