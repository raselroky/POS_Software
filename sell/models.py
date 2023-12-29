from django.db import models
from contact.models import Business_name,Customers
from user_management.models import CustomUser,Sales_Commission_Ager


PAYMENT_STATUS=(
    ('None','None'),
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
SHIPPING_STATUS=(
    ('None','None'),
    ('Ordered','Ordered'),
    ('Pending','Pending')
)

class Location_Set(models.Model):
    p_k=models.AutoField(primary_key=True)
    Location=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.Location
    

class All_Sales(models.Model):
    p_k=models.AutoField(primary_key=True)
    Created_At=models.DateTimeField(auto_now_add=True, blank=True)
    Invoice_No=models.TextField(null=True,blank=True)
    Customer_Name=models.ForeignKey(Business_name,on_delete=models.CASCADE,null=True,blank=True)
    Contact_Number=models.CharField(max_length=20,null=True,blank=True)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE,null=True,blank=True)
    Payment_Status=models.CharField(max_length=1000,choices=PAYMENT_STATUS,default='None')
    Payment_Method=models.CharField(max_length=1000,choices=PAYMENT_METHOD,default='None')
    Total_Amount=models.TextField(null=True,blank=True)
    Total_Paid=models.TextField(null=True,blank=True)
    Sell_Due=models.TextField(null=True,blank=True)
    Sell_Return_Due=models.TextField(null=True,blank=True)
    Shipping_Status=models.CharField(max_length=1000,null=True,blank=True)
    Shipping_Address=models.CharField(max_length=1000,null=True,blank=True)
    Total_Items=models.TextField(null=True,blank=True)
    Added_By=models.CharField(max_length=1000,null=True,blank=True) #Foreign key use User er

    def __str__(self):
        return str(self.Customer_Name.Business_Name)+' '+str(self.Location.Location)


class List_Draft(models.Model):
    p_k=models.AutoField(primary_key=True)
    Created_At=models.DateTimeField(auto_now_add=True, blank=True)
    Reference_No=models.TextField(null=True,blank=True)
    Customer_Name=models.ForeignKey(Business_name,on_delete=models.CASCADE,null=True,blank=True)
    Contact_Number=models.CharField(max_length=20,null=True,blank=True)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE,null=True,blank=True)
    Total_Items=models.TextField(null=True,blank=True)
    Added_By=models.CharField(max_length=1000,null=True,blank=True) #Foreignkey use User er

    def __str__(self):
        return str(self.Customer_Name.Business_Name)+' '+str(self.Location.Location)
    
    
class List_Sell_Return(models.Model):
    p_k=models.AutoField(primary_key=True)
    Created_At=models.DateTimeField(auto_now_add=True, blank=True)
    Invoice_No=models.TextField(null=True,blank=True)
    Parent_Sale=models.CharField(max_length=1000,null=True,blank=True)
    Customer_Name=models.ForeignKey(Business_name,on_delete=models.CASCADE,null=True,blank=True)
    Contact_Number=models.CharField(max_length=20,null=True,blank=True)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE,null=True,blank=True)
    Payment_Status=models.CharField(max_length=1000,choices=PAYMENT_STATUS,default='None')
    Total_Amount=models.TextField(null=True,blank=True)
    Payment_Due=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.Customer_Name.Business_Name
    


class Shipments(models.Model):
    p_k=models.AutoField(primary_key=True)
    Created_At=models.DateTimeField(auto_now_add=True, blank=True)
    Invoice_No=models.TextField(null=True,blank=True)
    Customer_Name=models.ForeignKey(Business_name,on_delete=models.CASCADE,null=True,blank=True)
    Contact_Number=models.CharField(max_length=20,null=True,blank=True)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE,null=True,blank=True)
    Shipping_Status=models.CharField(max_length=1000,choices=SHIPPING_STATUS,default='None')
    Payment_Status=models.CharField(max_length=1000,choices=PAYMENT_STATUS,default='None')
    Service_Staff=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return str(self.Customer_Name.Business_Name)+' '+str(self.Location.Location)
    

class Discount(models.Model):
    p_k=models.AutoField(primary_key=True)
    Name=models.ForeignKey(Business_name,on_delete=models.CASCADE)
    Starts_At=models.CharField(max_length=1000,null=True,blank=True)
    Ends_At=models.CharField(max_length=1000,null=True,blank=True)
    Discount_Amount=models.TextField(null=True,blank=True)
    Priority=models.CharField(max_length=1000,null=True,blank=True)
    Brand=models.CharField(max_length=1000,null=True,blank=True) #Foreignkey use Brand er
    Category=models.CharField(max_length=1000,null=True,blank=True) #Foreignkey use Categoryr
    Product=models.CharField(max_length=1000,null=True,blank=True)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return str(self.Name.Business_Name)+' '+str(self.Location.Location)


class Filter(models.Model):
    Business_Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE,null=True,blank=True)
    Customer=models.ForeignKey(Customers,on_delete=models.CASCADE,null=True,blank=True)
    Payment_Status=models.CharField(max_length=1000,choices=PAYMENT_STATUS,default='None')
    Date_Range=models.CharField(max_length=1000,null=True,blank=True)
    User=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    Sales_Commission_Agent=models.ForeignKey(Sales_Commission_Ager,on_delete=models.CASCADE,null=True,blank=True)
    Shipping_Status=models.CharField(max_length=1000,choices=SHIPPING_STATUS,default='None')

    def __str__(self):
        return self.Customer.Business_Name +' '+self.Customer.Email
        
    