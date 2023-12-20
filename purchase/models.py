from django.db import models
from contact.models import Suppliers,Customers,Business_name
from sell.models import Location_Set

PAY_TERM=(
    (0,'Select'),
    (1,'Daily'),
    (2,'Weekly'),
    (3,'Half of Month'),
    (4,'Monthly'),
    (5,'Half of Year'),
    (6,'Yearly')
)

PURCHASE_STATUS=(
    (0,'Due'), #red
    (1,'Recieved') #green
)

PAYMENT_STATUS=(
    (0,'Due'), #red
    (1,'Partial'), #blue
    (2,'Paid') #green
)


class Purchases(models.Model):
    p_k=models.AutoField(primary_key=True)
    Created_At=models.DateTimeField(auto_now_add=True, blank=True)
    Reference_No=models.CharField(max_length=1000,null=True,blank=True)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE,null=True,blank=True)
    Supplier=models.ForeignKey(Business_name,on_delete=models.CASCADE,null=True,blank=True)
    Purchase_Status=models.IntegerField(choices=PURCHASE_STATUS,default=0)
    Payment_Status=models.IntegerField(choices=PAYMENT_STATUS,default=0)
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
    Purchase_Status=models.IntegerField(choices=PURCHASE_STATUS,default=0)
    Address=models.CharField(max_length=1000,null=True,blank=True)
    Business_Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE,null=True,blank=True)
    Pay_Term=models.IntegerField(choices=PAY_TERM,default=0)
    Attached_Document=models.FileField(upload_to='Files/')

    def __str__(self):
        return self.Reference_No+' '+self.Address


class List_Purchase_Return(models.Model):
    p_k=models.AutoField(primary_key=True)
    Created_At=models.DateTimeField(auto_now_add=True, blank=True)
    Reference_No=models.CharField(max_length=1000,null=True,blank=True)
    Parent_Purchase=models.TextField(null=True,blank=True)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE,null=True,blank=True)
    Supplier=models.ForeignKey(Business_name,on_delete=models.CASCADE,null=True,blank=True)
    Payment_Status=models.IntegerField(choices=PAYMENT_STATUS,default=0)
    Grand_Total=models.TextField(null=True,blank=True)
    Payment_Due=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.Reference_No+' '+self.Location.Location
    