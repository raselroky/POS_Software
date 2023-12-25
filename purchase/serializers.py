from rest_framework import serializers
from .models import Purchases,Add_Purchase,List_Purchase_Return,Additional_Expense

class Purchases_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Purchases
        fields=('__all__')
        
class Purchases_All_Show_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Purchases
        fields=('__all__')
        depth=1

class Add_Purchases_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Add_Purchase
        fields=('__all__')
class Add_Purchases_All_Show_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Add_Purchase
        fields=('__all__')
        depth=1
    
class List_Purchase_Return_Serializer(serializers.ModelSerializer):
    class Meta:
        model=List_Purchase_Return
        fields=('__all__')
class List_Purchase_Return_All_Show_Serializer(serializers.ModelSerializer):
    class Meta:
        model=List_Purchase_Return
        fields=('__all__')
        depth=1

class Additonal_Expense_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Additional_Expense
        fields=('__all__')