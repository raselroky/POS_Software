from rest_framework import serializers
from . models import Sales,Sale_Purchase,Due_Amount,Purchases,Supplier_And_Customer_Report,Input_Tax,Output_Tax,Expense_Tax,Customer_Group_Report,Stock_Adjustment_Report,Item_Report,Product_Purchase_Report,Product_Sell_Report,Purchase_Payment_Report,Sell_Payment_Report,Expense_Report,Register_Report,Sales_Report_Added,Sales_Report_With_Commission,Sales_Report_Expense,Stock_Report,Expense_Categories_List

class Purchase_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Purchases
        fields=('__all__')
        
class Sales_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Sales
        fields=('__all__')

class Sale_Purchase_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Sale_Purchase
        fields=('__all__')
class Due_Amount_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Due_Amount
        fields=('__all__')
class Input_Tax_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Input_Tax
        fields=('__all__')
class Output_Tax_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Output_Tax
        fields=('__all__')
class Expense_Tax_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Expense_Tax
        fields=('__all__')
class Supplier_And_Customer_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Supplier_And_Customer_Report
        fields=('__all__')
class Customer_Group_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Customer_Group_Report
        fields=('__all__')
class Stock_Adjustment_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Stock_Adjustment_Report
        fields=('__all__')
class Item_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Item_Report
        fields=('__all__')
class Product_Purchase_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Product_Purchase_Report
        fields=('__all__')

class Product_Sell_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Product_Sell_Report
        fields=('__all__')

class Purchase_Payment_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Purchase_Payment_Report
        fields=('__all__')

class Sell_Payment_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Sell_Payment_Report
        fields=('__all__')

class Expense_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Expense_Report
        fields=('__all__')

class Register_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Register_Report
        fields=('__all__')

class Sales_Report_Added_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Sales_Report_Added
        fields=('__all__')

class Sales_Report_With_Commission_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Sales_Report_With_Commission
        fields=('__all__')

class Sales_Report_Expense_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Sales_Report_Expense
        fields=('__all__')

class Stock_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Stock_Report
        fields=('__all__')

class Expense_Categories_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Expense_Categories_List
        fields=('__all__')