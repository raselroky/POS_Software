from django.db import models
from datetime import datetime    


PAY_TERM=(
    ('Select','Select'),
    ('Daily','Daily'),
    ('Weekly','Weekly'),
    ('Half of Month','Half of Month'),
    ('Monthly','Monthly'),
    ('Half of Year','Half of Year'),
    ('Yearly','Yearly')
)

ACTION_STATUS=(
    ('Action','Action'),
    ('Pay','Pay'),
    ('View','View'),
    ('Edit','Edit'),
    ('Delete','Delete'),
    ('Deactivate','Deactivate'),
    ('Ledger','Ledger'),
    ('Purchase','Purchase'),
    ('Stock Report','Stock Report'),
    ('Documents & Note','Documents & Note')
)

PAID_STATUS=(
    ('Checking','Checking'),
    ('Payment Done','Payment Done'),
    ('Due Running','Due Running'),
    ('Return Due Running','Return Due Running')
)

class Action(models.Model):
    Actions=models.CharField(max_length=1000,choices=ACTION_STATUS,default='Action')

class Customer_Group(models.Model):
    p_k=models.AutoField(primary_key=True)
    Customer_Group_Name=models.CharField(max_length=1000,null=True,blank=True)
    Calculation_Percentage=models.CharField(max_length=1000,null=True,blank=True)
    Selling_Price_Group=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.Customer_Group_Name
    
class Business_name(models.Model):
    p_k=models.AutoField(primary_key=True)
    Business_Name=models.CharField(max_length=1000,null=True,blank=True)
    Category=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.Business_Name

class Contact_id(models.Model):
    p_k=models.AutoField(primary_key=True)
    Contact_Ids=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return f'{self.Contact_Ids}'
    


class Suppliers(models.Model):
    p_k=models.AutoField(primary_key=True)
    Contact_ID=models.ForeignKey(Contact_id,on_delete=models.CASCADE,null=True,blank=True)
    Business_Name=models.ForeignKey(Business_name,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=1000,null=True,blank=True)
    Email=models.EmailField(max_length=1000,unique=True,null=True,blank=True)
    Address=models.CharField(max_length=1000,null=True,blank=True)
    Mobile=models.CharField(max_length=20,unique=True,null=True,blank=True)
    Supplier_group=models.ForeignKey(Customer_Group,on_delete=models.CASCADE,null=True,blank=True)
    Tax_Number=models.TextField(unique=True,blank=True,null=True)
    Pay_Term=models.CharField(max_length=1000,choices=PAY_TERM,default='Select')
    Opening_Balance_Due=models.TextField(null=True,blank=True)
    Total_Amount=models.TextField(null=True,blank=True)
    Advance_Amount=models.TextField(null=True,blank=True)
    Due_Amount=models.TextField(null=True,blank=True)
    Return_Due_Amount=models.TextField(null=True,blank=True)
    Paid_Status=models.CharField(max_length=1000,choices=PAID_STATUS,default='Checking')
    Created_At=models.DateTimeField(auto_now_add=True, null=True,blank=True)

    def __str__(self):
        return self.Email
    

class Customers(models.Model):
    p_k=models.AutoField(primary_key=True)
    Contact_ID=models.ForeignKey(Contact_id,on_delete=models.CASCADE,null=True,blank=True)
    Business_Name=models.ForeignKey(Business_name,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=1000,null=True,blank=True)
    Email=models.EmailField(max_length=1000,unique=True,null=True,blank=True)
    Mobile=models.CharField(max_length=20,unique=True,null=True,blank=True)
    Delivery_Address=models.CharField(max_length=1000,null=True,blank=True)
    Home_Address=models.CharField(max_length=1000,null=True,blank=True)
    Tax_Number=models.TextField(unique=True,blank=True,null=True)
    Credit_limit=models.TextField(null=True,blank=True)
    Reward_Point=models.TextField(null=True,blank=True)
    Customer_group=models.ForeignKey(Customer_Group,on_delete=models.CASCADE,null=True,blank=True)
    Pay_Term=models.CharField(max_length=1000,choices=PAY_TERM,default='Select')
    Opening_Balance=models.TextField(null=True,blank=True)
    Opening_Balance_Due=models.TextField(null=True,blank=True)
    Advance_Balance=models.TextField(null=True,blank=True)
    Total_Sale_Due=models.TextField(null=True,blank=True)
    Total_Sell_Return_Due=models.TextField(null=True,blank=True)
    Shipping_Address=models.CharField(max_length=1000,null=True,blank=True)
    Created_At=models.DateTimeField(auto_now_add=True, null=True,blank=True)

    def __str__(self):
        return self.Email
    
 