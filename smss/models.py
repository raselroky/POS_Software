from django.db import models

class All_Number(models.Model):
    p_k=models.AutoField(primary_key=True)
    Number=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return str(self.p_k)

class All_Number_Sms(models.Model):
    p_k=models.AutoField(primary_key=True)
    sms=models.TextField(null=True,blank=True)
    numbers=models.ManyToManyField(All_Number)

    def __str__(self):
        return str(self.p_k)


class All_Supplier_Number(models.Model):
    p_k=models.AutoField(primary_key=True)
    number=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return str(self.p_k)
    
class All_Supplier_Number_Smss(models.Model):
    p_k=models.AutoField(primary_key=True)
    sms=models.TextField(null=True,blank=True)
    numbers=models.ManyToManyField(All_Supplier_Number)

    def __str__(self):
        return str(self.p_k)



class All_Customer_Number(models.Model):
    p_k=models.AutoField(primary_key=True)
    number=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return str(self.p_k)

class All_Customer_Number_Smss(models.Model):
    p_k=models.AutoField(primary_key=True)
    sms=models.TextField(null=True,blank=True)
    numbers=models.ManyToManyField(All_Customer_Number)

    def __str__(self):
        return str(self.p_k)
    