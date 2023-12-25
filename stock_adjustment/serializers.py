from rest_framework import serializers
from .models import Stock_Adjustment

class Stock_Adjustment_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Stock_Adjustment
        fields=('__all__')
        