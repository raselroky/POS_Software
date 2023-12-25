from django.db import models
from sell.models import PAYMENT_METHOD

ACTION_STATUS=(
    ('Action','Action'),
    ('View','View'),
    ('Edit','Edit'),
    ('Delete','Delete')
)


class Account_type(models.Model):
    p_k=models.AutoField(primary_key=True)
    account_type=models.CharField(max_length=1000)

    def __str__(self):
        return self.account_type
    


class List_Account(models.Model):
    p_k=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=1000,null=True,blank=True)
    Account_Type=models.ForeignKey(Account_type,on_delete=models.CASCADE,null=True,blank=True)
    Account_Number=models.TextField(null=True,blank=True)
    Note=models.CharField(max_length=1000,null=True,blank=True)
    Balance=models.TextField(null=True,blank=True)
    Account_Details=models.TextField(null=True,blank=True)
    Added_By=models.CharField(max_length=1000,null=True,blank=True)
    Action=models.CharField(max_length=1000,choices=ACTION_STATUS,default='Action')

    def __str__(self):
        return self.Name +' '+self.Account_Number
    
#Balance Sheet
class Liability(models.Model):
    p_k=models.AutoField(primary_key=True)
    Liability_Name=models.TextField(null=True,blank=True)
    Total_Liability=models.TextField(null=True,blank=True)
    

class Assets(models.Model):
    p_k=models.AutoField(primary_key=True)
    Asset_Name=models.TextField(null=True,blank=True)
    Total_Assets=models.TextField(null=True,blank=True)


class Trial_Balance(models.Model):
    p_k=models.AutoField(primary_key=True)
    Trial_Balance_Name=models.TextField(null=True,blank=True)
    Debit=models.TextField(null=True,blank=True)
    Credit=models.TextField(null=True,blank=True)
    

class Cash_Flow(models.Model):
    p_k=models.AutoField(primary_key=True)
    Date=models.DateTimeField(auto_now_add=True, null=True,blank=True)
    Account=models.ForeignKey(Account_type,on_delete=models.CASCADE,null=True,blank=True)
    Description=models.CharField(max_length=1000,null=True,blank=True)
    Payment_Method=models.CharField(max_length=1000,choices=PAYMENT_METHOD,default='None')
    Payment_Details=models.CharField(max_length=1000,null=True,blank=True)
    Debit=models.TextField(null=True,blank=True)
    Credit=models.TextField(null=True,blank=True)
    Account_Balance=models.TextField(null=True,blank=True)
    Total_Balance=models.TextField(null=True,blank=True)

class Payment_Account_Report(models.Model):
    p_k=models.AutoField(primary_key=True)
    Date=models.DateTimeField(auto_now_add=True, null=True,blank=True)
    Payment_Reference_No=models.CharField(max_length=1000,null=True,blank=True)
    Invoice_Or_Reference_No=models.CharField(max_length=1000,null=True,blank=True)
    Amount=models.TextField(null=True,blank=True)
    Payment_Type=models.CharField(max_length=1000,null=True,blank=True)
    Description=models.CharField(max_length=1000,null=True,blank=True)
    Action=models.ForeignKey(Account_type,on_delete=models.CASCADE,null=True,blank=True)