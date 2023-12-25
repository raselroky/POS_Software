
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from smss.models import All_Number
from django.contrib.auth.models import Group, Permission

PAY_TERM=(
    ('Select','Select'),
    ('Daily','Daily'),
    ('Weekly','Weekly'),
    ('Half of Month','Half of Month'),
    ('Monthly','Monthly'),
    ('Half of Year','Half of Year'),
    ('Yearly','Yearly')
)

ACTION=(
    ('Select','Select'),
    ('View','View'),
    ('Edit','Edit'),
    ('Delete','Delete')
)
GENDER=(
    ('Please Select','Please Select'),
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
)
MARITAL_STATUS=(
    ('Marital Status','Marital Status'),
    ('Married','Married'),
    ('Unmarried','Unmarried'),
    ('Divorce','Divorce')
)

class Roles(models.Model):
    #p_k=models.AutoField(primary_key=True)
    Role=models.CharField(max_length=1000,null=True,blank=True)
    groups = models.ManyToManyField(
        Group,
        #null=True,
        blank=True,
        related_name='customuser_set',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        #null=True,
        blank=True,
        related_name='customuser_set',
    )

    def __str__(self):
        return str(self.Role)
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    #p_k=models.AutoField(primary_key=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    first_name = models.CharField(max_length=30,null=True,blank=True)
    last_name = models.CharField(max_length=30,null=True,blank=True)
    is_active = models.BooleanField(default=True,null=True,blank=True)
    is_staff = models.BooleanField(default=False,null=True,blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    mobile_number = models.CharField(max_length=20, unique=True,null=True)
    position=models.CharField(max_length=500,null=True,blank=True)
    image=models.ImageField(upload_to='images/',blank=True, null=True)

    #roles and permission
    Role=models.ForeignKey(Roles,on_delete=models.CASCADE,blank=True, null=True)

    #sales 
    Sales_Commission_Percentage=models.CharField(max_length=1000,null=True,blank=True)
    Max_Sales_Discount_Percentage=models.CharField(max_length=1000,null=True,blank=True)
    contact=models.ForeignKey(All_Number,on_delete=models.CASCADE,blank=True, null=True)

    #More Information
    Date_Of_Birth=models.CharField(max_length=1000,null=True,blank=True)
    Gender=models.CharField(max_length=1000,choices=GENDER,default='Please Select')
    Marital_Status=models.CharField(max_length=1000,choices=MARITAL_STATUS,default='Marital Status')
    Blood_Group=models.CharField(max_length=1000,null=True,blank=True)
    Phone_Number=models.CharField(max_length=1000,null=True,blank=True)
    Alternate_Contact_Number=models.CharField(max_length=1000,null=True,blank=True)
    Family_Contact_Number=models.CharField(max_length=1000,null=True,blank=True)
    Facebook_Link=models.CharField(max_length=1000,null=True,blank=True)
    Twitter_Link=models.CharField(max_length=1000,null=True,blank=True)
    Permanent_Address=models.CharField(max_length=1000,null=True,blank=True)
    Current_Address=models.CharField(max_length=1000,null=True,blank=True)

    #bank Details
    Account_Holders_Name=models.CharField(max_length=1000,null=True,blank=True)
    Account_Number=models.CharField(max_length=1000,null=True,blank=True)
    Bank_Name=models.CharField(max_length=1000,null=True,blank=True)
    Bank_Identifier_Code=models.CharField(max_length=1000,null=True,blank=True)
    Branch=models.CharField(max_length=1000,null=True,blank=True)
    Tax_Payer_ID=models.CharField(max_length=1000,null=True,blank=True)

    #payroll 
    Basic_Salary=models.TextField(null=True,blank=True)
    Pay_Term=models.CharField(max_length=1000,choices=PAY_TERM,default='Select')
    Pay_Components=models.CharField(max_length=1000,null=True,blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['first_name', 'last_name']

    # this thing is need to avoid some wird error i didn't figure out
    # so i just didn't show it in serializers.py
   
    #----------------------------------
    def __str__(self):
        return self.email





class Sales_Commission_Ager(models.Model):
    #p_k=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=1000,null=True,blank=True)
    Email=models.CharField(max_length=1000,null=True,blank=True,unique=True)
    Contact_Number=models.CharField(max_length=1000,null=True,blank=True,unique=True)
    Address=models.CharField(max_length=1000,null=True,blank=True)
    Sales_Commission_Percentage=models.CharField(max_length=1000,null=True,blank=True)
    Action=models.CharField(max_length=1000,choices=ACTION,default='Select')

    def __str__(self):
        return self.Name
    

class  Adds(models.Model):
    #p_k=models.AutoField(primary_key=True)
    Prefix=models.CharField(max_length=1000,null=True,blank=True)
    First_Name=models.CharField(max_length=1000,null=True,blank=True)
    Last_Name=models.CharField(max_length=1000,null=True,blank=True)
    Email=models.CharField(max_length=1000,null=True,blank=True,unique=True)
    Contact_Number=models.CharField(max_length=1000,null=True,blank=True,unique=True)
    Address=models.CharField(max_length=1000,null=True,blank=True)
    Sales_Commission_Percentage=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.Prefix



    
    
