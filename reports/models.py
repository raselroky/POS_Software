from django.db import models

class All_Reports(models.Model):
    p_k=models.AutoField(primary_key=True)
    #Gross_Profit=models.TextField(null=True,blank=True)
    #Net_Profit=models.TextField(null=True,blank=True)
    #Total_Sales=models.TextField(null=True,blank=True)
    Total_Products_Item=models.TextField(null=True,blank=True)
    Total_Purchase=models.TextField(null=True,blank=True)
    #Total_Sell_Shipping_Charge=models.TextField(null=True,blank=True)
    #Current_Stock=models.TextField(null=True,blank=True)
    #Total_Purchase_Shipping_Charge=models.TextField(null=True,blank=True)
    #Total_Sell_Discount=models.TextField(null=True,blank=True)
    #Total_Expense=models.TextField(null=True,blank=True)
    #Total_Purchase_Discount=models.TextField(null=True,blank=True)
    Total_Sell_Return=models.TextField(null=True,blank=True)
    Total_Customer_Due=models.TextField(null=True,blank=True)
    Total_Supplier_Due=models.TextField(null=True,blank=True)
    #Total_Sell_Round_Off=models.TextField(null=True,blank=True)
    Total_Customer_Opening_Balance_Due=models.TextField(null=True,blank=True)
    Total_Supplier_Opening_Balance_Due=models.TextField(null=True,blank=True)

    
    
