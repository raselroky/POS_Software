from rest_framework import serializers
from .models import All_Sales,List_Draft,Shipments,Discount,Location_Set,List_Sell_Return,Filter

class Location_Set_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Location_Set
        fields=('__all__')

class All_Sales_Serializer(serializers.ModelSerializer):
    class Meta:
        model=All_Sales
        fields=('__all__')
class All_Sales__All_Show_Serializer(serializers.ModelSerializer):
    class Meta:
        model=All_Sales
        fields=('__all__')
        depth=1

class List_Draft_Serializer(serializers.ModelSerializer):
    class Meta:
        model=List_Draft
        fields=('__all__')
class List_Draft_All_Show_Serializer(serializers.ModelSerializer):
    class Meta:
        model=List_Draft
        fields=('__all__')
        depth=1

class List_Sell_Return_Serializer(serializers.ModelSerializer):
    class Meta:
        model=List_Sell_Return
        fields=('__all__')
class List_Sell_Return_All_Show_Serializer(serializers.ModelSerializer):
    class Meta:
        model=List_Sell_Return
        fields=('__all__')
        depth=1

class Shipments_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Shipments
        fields=('__all__')
class Shipments_All_Show_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Shipments
        fields=('__all__')
        depth=1


class Discount_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Discount
        fields=('__all__')
class Discount_All_Show_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Discount
        fields=('__all__')
        depth=1

class Filter_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Filter
        fields=('__all__')