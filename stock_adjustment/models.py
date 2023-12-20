from django.db import models
from sell.models import Location_Set

ACTIONS=(
    (0,'None'),
    (1,'View'),
    (2,'Delete')
)

class Stock_Adjustment(models.Model):
    p_k=models.AutoField(primary_key=True)
    Action=models.IntegerField(choices=ACTIONS,default=0,null=True,blank=True)
    Date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    Reference_No=models.CharField(max_length=1000,null=True,blank=True)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE,null=True,blank=True)
    Adjustment_Type=models.CharField(max_length=1000,null=True,blank=True)
    Total_Amount=models.TextField(null=True,blank=True)
    Total_Amount_Recovered=models.TextField(null=True,blank=True)
    Reason=models.CharField(max_length=1000,null=True,blank=True)
    Added_By=models.CharField(max_length=1000,null=True,blank=True)
    
