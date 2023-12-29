from django.db import models
from contact.models import Suppliers,Customers,Business_name
from sell.models import Location_Set
from payment_account.models import Account_type
from user_management.models import CustomUser,Sales_Commission_Ager

DISCOUNT_TYPE=(
    ('Please Select','Please Select'),
    ('Percentage','Percentage'),
    ('Fixed','Fixed')
)
SHIPPING_STATUS=(
    ('Select','Select'),
    ('Ordered','Ordered'),
    ('Packed','Packed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)
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

class Add_Quotation(models.Model):
    p_k=models.AutoField(primary_key=True)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE)
    Customer=models.ForeignKey(Customers,on_delete=models.CASCADE)
    Pay_Term=models.CharField(max_length=1000,choices=PAY_TERM,default='Select')
    Commssion_Agent=models.ForeignKey(Sales_Commission_Ager,on_delete=models.CASCADE)
    Sale_Date=models.DateTimeField(null=True,blank=True)
    Billing_Address=models.CharField(max_length=1000,null=True,blank=True)
    Shipping_Address=models.CharField(max_length=1000,null=True,blank=True)
    Invoice_Number=models.CharField(max_length=1000,null=True,blank=True)
    Attach_Document=models.FileField(upload_to='Files/')

    Discount_Type=models.CharField(max_length=1000,choices=DISCOUNT_TYPE,default='Please Select')
    Discount_Amount=models.TextField(null=True,blank=True)
    Order_Tax=models.TextField(null=True,blank=True)
    Sell_Note=models.CharField(max_length=1000,null=True,blank=True)

    Shipping_Details=models.CharField(max_length=1000,null=True,blank=True)
    Shipping_Addresss=models.CharField(max_length=1000,null=True,blank=True)
    Shipping_Charges=models.TextField(null=True,blank=True)
    Shipping_Status=models.CharField(max_length=1000,choices=SHIPPING_STATUS,default='Select')
    Shipping_Document=models.FileField(upload_to='Files/')

    def __str__(self):
        return self.Customer.Business_Name

    
