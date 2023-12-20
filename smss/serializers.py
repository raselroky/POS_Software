from rest_framework import serializers
from .models import All_Number,All_Number_Sms,All_Supplier_Number,All_Supplier_Number_Smss,All_Customer_Number,All_Customer_Number_Smss

class All_Number_Serializer(serializers.ModelSerializer):
    class Meta:
        model=All_Number
        fields=('__all__')
class All_Number_Sms_Serializer(serializers.ModelSerializer):
    class Meta:
        model=All_Number_Sms
        fields=('__all__')


class All_Supplier_Number_Serializer(serializers.ModelSerializer):
    class Meta:
        model=All_Supplier_Number
        fields=('__all__')
class All_Supplier_Number_Smss_Serializer(serializers.ModelSerializer):
    class Meta:
        model=All_Supplier_Number_Smss
        fields=('__all__')


class All_Customer_Number_Serializer(serializers.ModelSerializer):
    class Meta:
        model=All_Customer_Number
        fields=('__all__')
class All_Customer_Number_Smss_Serializer(serializers.ModelSerializer):
    class Meta:
        model=All_Customer_Number_Smss
        fields=('__all__')
