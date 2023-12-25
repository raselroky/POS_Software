from django.db import models
from contact.models import Suppliers,Customers,Business_name
from sell.models import Location_Set
from payment_account.models import Account_type

PAY_TERM=(
    ('Select','Select'),
    ('Daily','Daily'),
    ('Weekly','Weekly'),
    ('Half of Month','Half of Month'),
    ('Monthly','Monthly'),
    ('Half of Year','Half of Year'),
    ('Yearly','Yearly')
)

PURCHASE_STATUS=(
    ('Due','Due'), #red
    ('Recieved','Recieved') #green
)

PAYMENT_STATUS=(
    ('Due','Due'), #red
    ('Partial','Partial'), #blue
    ('Paid','Paid') #green
)

PAYMENT_METHOD=(
    ('None','None'),
    ('Cash','Cash'),
    ('Check','Check'),
    ('Bank-Card','Bank-Card'),
    ('Bkash','Bkash'),
    ('Nagad','Nagad'),
    ('Upay','Upay')
)

class Additional_Expense(models.Model):
    p_k=models.AutoField(primary_key=True)
    Expense_Name=models.CharField(max_length=1000,null=True,blank=True)
    Amount=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.Expense_Name
    

class Purchases(models.Model):
    p_k=models.AutoField(primary_key=True)
    Created_At=models.DateTimeField(auto_now_add=True, blank=True)
    Reference_No=models.CharField(max_length=1000,null=True,blank=True)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE,null=True,blank=True)
    Supplier=models.ForeignKey(Business_name,on_delete=models.CASCADE,null=True,blank=True)
    Purchase_Status=models.CharField(max_length=1000,choices=PURCHASE_STATUS,default='Due')
    Payment_Status=models.CharField(max_length=1000,choices=PAYMENT_STATUS,default='Due')
    Grand_Total=models.TextField(null=True,blank=True)
    Payment_Due=models.TextField(null=True,blank=True)
    Added_By=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.Reference_No+' '+self.Location.Location


class Add_Purchase(models.Model):
    p_k=models.AutoField(primary_key=True)
    Supplier=models.ForeignKey(Business_name,on_delete=models.CASCADE,null=True,blank=True)
    Reference_No=models.CharField(max_length=1000,null=True,blank=True)
    Purchase_Date=models.DateTimeField(auto_now_add=True, blank=True)
    Purchase_Status=models.CharField(max_length=1000,choices=PURCHASE_STATUS,default='Due')
    Address=models.CharField(max_length=1000,null=True,blank=True)
    Business_Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE,null=True,blank=True)
    Pay_Term=models.CharField(max_length=1000,choices=PAY_TERM,default='Select')
    Attached_Document=models.FileField(upload_to='Files/')

    Discount_Type=models.CharField(max_length=1000,null=True,blank=True)
    Discount_Amount=models.TextField(null=True,blank=True)
    Purchase_Tax=models.TextField(null=True,blank=True)
    Additional_Notes=models.TextField(null=True,blank=True)

    Shipping_Details=models.CharField(max_length=1000,null=True,blank=True)
    Additional_Shipping_Charges=models.TextField(null=True,blank=True)

    Addition_expense=models.ForeignKey(Additional_Expense,on_delete=models.CASCADE,null=True,blank=True)

    #Add_Payment
    Amount=models.TextField(null=True,blank=True)
    Paid_On=models.DateTimeField(auto_now_add=True)
    Payment_Method=models.CharField(max_length=1000,choices=PAYMENT_METHOD,default='None')
    Payment_Account=models.ForeignKey(Account_type,on_delete=models.CASCADE,null=True,blank=True)
    Payment_Note=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.Reference_No+' '+self.Address


class List_Purchase_Return(models.Model):
    p_k=models.AutoField(primary_key=True)
    Created_At=models.DateTimeField(auto_now_add=True, blank=True)
    Reference_No=models.CharField(max_length=1000,null=True,blank=True)
    Parent_Purchase=models.TextField(null=True,blank=True)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE,null=True,blank=True)
    Supplier=models.ForeignKey(Business_name,on_delete=models.CASCADE,null=True,blank=True)
    Payment_Status=models.CharField(max_length=1000,choices=PAYMENT_STATUS,default='Due')
    Grand_Total=models.TextField(null=True,blank=True)
    Payment_Due=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.Reference_No+' '+self.Location.Location
    