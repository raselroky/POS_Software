from rest_framework import serializers
from .models import Purchases,Add_Purchase,List_Purchase_Return

class Purchases_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Purchases
        fields=('__all__')

class Add_Purchases_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Add_Purchase
        fields=('__all__')
    
class List_Purchase_Return_Serializer(serializers.ModelSerializer):
    class Meta:
        model=List_Purchase_Return
        fields=('__all__')