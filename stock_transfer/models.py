from django.db import models

STATUS=(
    (0,'Pending'),
    (1,'Completed'),
    (2,'In Transit')
)

class Stock_Transfer(models.Model):
    p_k=models.AutoField(primary_key=True)
    Date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    Reference_No=models.CharField(max_length=1000,null=True,blank=True)
    Location_From=models.CharField(max_length=1000,null=True,blank=True)
    Location_To=models.CharField(max_length=1000,null=True,blank=True)
    Status=models.IntegerField(choices=STATUS,default=0)
    Shipping_Charges=models.TextField(null=True,blank=True)
    Total_Amount=models.TextField(null=True,blank=True)
    Additional_Notes=models.CharField(max_length=1000,null=True,blank=True)

    
