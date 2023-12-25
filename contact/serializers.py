from rest_framework import serializers
from .models import Suppliers,Customers,Customer_Group,Business_name,Contact_id


class Customers_Group_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Customer_Group
        fields=('__all__')

class Business_name_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Business_name
        fields=('__all__')

class Contact_id_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Contact_id
        fields=('__all__')

class Suppliers_Serializer(serializers.ModelSerializer):
    #Contact_ID=Contact_id_Serializer(many=True)
    class Meta:
        model=Suppliers
        fields=('__all__')

class Suppliers_All_Show_Serializer(serializers.ModelSerializer):
    #Contact_ID=Contact_id_Serializer(many=True)
    class Meta:
        model=Suppliers
        fields=('__all__')
        depth=2

class Customers_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields=('__all__')

class Customers_All_Show_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields=('__all__')
        depth=2
        

