from rest_framework import serializers
from .models import List_Account,Account_type,Liability,Assets,Trial_Balance,Cash_Flow,Payment_Account_Report

class List_Account_Serializer(serializers.ModelSerializer):
    class Meta:
        model=List_Account
        fields=('__all__')

class Account_type_Serialzer(serializers.ModelSerializer):
    class Meta:
        model=Account_type
        fields=('__all__')

class Liability_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Liability
        fields=('__all__')

class Assets_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Assets
        fields=('__all__')

class Trial_Balance_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Trial_Balance
        fields=('__all__')

class Cash_Flow_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Cash_Flow
        fields=('__all__')

class Payment_Account_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Payment_Account_Report
        fields=('__all__')