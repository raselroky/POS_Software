from django.db import models
from contact.models import Business_name,Customer_Group,Contact_id,ACTION_STATUS
from sell.models import Location_Set,PAYMENT_METHOD

class Purchases(models.Model):
    p_k=models.AutoField(primary_key=True)
    Total_Purchase=models.TextField(null=True,blank=True)
    Purchase_Including_Tax=models.TextField(null=True,blank=True)
    Total_Purchase_Return_Including_Tax=models.TextField(null=True,blank=True)
    Purchase_Deu=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.Total_Purchase)
    
        
class Sales(models.Model):
    p_k=models.AutoField(primary_key=True)
    Total_Sale=models.TextField(null=True,blank=True)
    Sale_Including_Tax=models.TextField(null=True,blank=True)
    Total_Sell_Return_Including_Tax=models.TextField(null=True,blank=True)
    sale_Due=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.Total_Sale)
    

class Sale_Purchase(models.Model):
    p_k=models.AutoField(primary_key=True)
    Sale_purchase=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.Sale_purchase
    
class Due_Amount(models.Model):
    p_k=models.AutoField(primary_key=True)
    Due_amount=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.Due_amount
    
    
    
class Input_Tax(models.Model):
    p_k=models.AutoField(primary_key=True)
    Date=models.DateTimeField(auto_now_add=True)
    Reference_No=models.CharField(max_length=1000,null=True,blank=True)
    Supplier=models.ForeignKey(Business_name,on_delete=models.CASCADE)
    Tax_Number=models.TextField(null=True,blank=True)
    Total_Amount=models.TextField(null=True,blank=True)
    Payment_Method=models.CharField(max_length=1000,null=True,blank=True)
    Discount=models.TextField(null=True,blank=True)
    Vat=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.Supplier.Business_Name)+' '+str(self.Reference_No)

class Output_Tax(models.Model):
    p_k=models.AutoField(primary_key=True)
    Date=models.DateTimeField(auto_now_add=True)
    Invoice_No=models.CharField(max_length=1000,null=True,blank=True)
    Customer=models.ForeignKey(Business_name,on_delete=models.CASCADE)
    Tax_Number=models.TextField(null=True,blank=True)
    Total_Amount=models.TextField(null=True,blank=True)
    Payment_Method=models.CharField(max_length=1000,null=True,blank=True)
    Discount=models.TextField(null=True,blank=True)
    Vat=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return str(self.Customer.Business_Name)+' '+str(self.Invoice_No)

class Expense_Tax(models.Model):
    p_k=models.AutoField(primary_key=True)
    Date=models.DateTimeField(auto_now_add=True)
    Invoice_No=models.CharField(max_length=1000,null=True,blank=True)
    Tax_Number=models.TextField(null=True,blank=True)
    Total_Amount=models.TextField(null=True,blank=True)
    Payment_Method=models.CharField(max_length=1000,null=True,blank=True)
    Vat=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.Invoice_No
    
    
    
class Supplier_And_Customer_Report(models.Model):
    p_k=models.AutoField(primary_key=True)
    Contact=models.ForeignKey(Business_name,on_delete=models.CASCADE)
    Total_Purchase=models.TextField(null=True,blank=True)
    Total_Purchase_Return=models.TextField(null=True,blank=True)
    Total_Sale=models.TextField(null=True,blank=True)
    Total_Sell_Return=models.TextField(null=True,blank=True)
    Opening_Balance_Due=models.TextField(null=True,blank=True)
    Due=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.Contact.Business_Name)


class Customer_Group_Report(models.Model):
    p_k=models.AutoField(primary_key=True)
    Customer_group=models.ForeignKey(Customer_Group,on_delete=models.CASCADE)
    Total_Sale=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.Customer_group.Customer_Group_Name


class Stock_Adjustment_Report(models.Model):
    p_k=models.AutoField(primary_key=True)
    Date=models.DateTimeField(auto_now_add=True)
    Reference_No=models.CharField(max_length=1000,null=True,blank=True)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE)
    Adjustment_Type=models.CharField(max_length=1000,null=True,blank=True)
    Total_Amount=models.TextField(null=True,blank=True)
    Total_Amount_Recovered=models.TextField(max_length=1000,null=True,blank=True)
    Reason=models.CharField(max_length=1000,null=True,blank=True)
    Added_By=models.CharField(max_length=1000,null=True,blank=True) #Foreignkey use User era 

    def __str__(self):
        return str(self.Reference_No)+' '+str(self.Location.Location)

    
class Item_Report(models.Model):
    p_k=models.AutoField(primary_key=True)
    Product=models.CharField(max_length=1000,null=True,blank=True) #Foreignkey use product er ,but check field lageb ki na,na lagle dorkar nai
    SKU=models.CharField(max_length=1000,null=True,blank=True) #Foreignkey SKU er
    Description=models.CharField(max_length=1000,null=True,blank=True)
    Purchase_Date=models.DateTimeField(auto_now_add=True)
    Purchase=models.CharField(max_length=1000,null=True,blank=True)
    Lot_Number=models.TextField(null=True,blank=True)
    Supplier=models.ForeignKey(Business_name,on_delete=models.CASCADE,related_name='supplier',db_column='supplier',)
    Purchase_Price=models.TextField(null=True,blank=True)
    Sell_Date=models.DateTimeField(auto_now_add=True)
    Sale=models.TextField(null=True,blank=True)
    Customer=models.ForeignKey(Business_name,on_delete=models.CASCADE,related_name='customer',db_column='customer',)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE,null=True,blank=True)
    Sell_Quantity=models.TextField(null=True,blank=True)
    Selling_Price=models.TextField(null=True,blank=True)
    Subtotal=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.Supplier.Business_Name)+' '+str(self.Location.Location)

class Product_Purchase_Report(models.Model):
    p_k=models.AutoField(primary_key=True)
    Product=models.CharField(max_length=1000,null=True,blank=True) #Foreignkey Product er,but check diye kon feild dorkar ekhane
    SKU=models.CharField(max_length=1000,null=True,blank=True) #Foreignkey SKU er 
    Supplier=models.ForeignKey(Business_name,on_delete=models.CASCADE)
    Reference_No=models.CharField(max_length=1000,null=True,blank=True)
    Date=models.DateTimeField(auto_now_add=True)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE)
    Quantity=models.TextField(null=True,blank=True)
    Total_Unit_Adjusted=models.CharField(max_length=1000,null=True,blank=True)
    Unit_Purchase_Price=models.TextField(null=True,blank=True)
    Subtotal=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return str(self.Supplier.Business_Name)+' '+str(self.Location.Location)


class Product_Sell_Report(models.Model):
    p_k=models.AutoField(primary_key=True)
    Product=models.CharField(max_length=1000,null=True,blank=True) #product er jodi kiso lagey foreignkey use korben
    SKU=models.CharField(max_length=1000,null=True,blank=True) #Foreignkey SKU er ta
    Customer_Name=models.ForeignKey(Business_name,on_delete=models.CASCADE)
    Contact_Id=models.ForeignKey(Contact_id,on_delete=models.CASCADE)
    Invoice_No=models.TextField(null=True,blank=True)
    Date=models.DateTimeField(auto_now_add=True)
    Quantity=models.TextField(null=True,blank=True)
    Unit_Price=models.TextField(null=True,blank=True)
    Discount=models.TextField(null=True,blank=True)
    Tax=models.TextField(null=True,blank=True)
    Price_Inc_Tax=models.TextField(null=True,blank=True)
    Total=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.Product)+' '+str(self.Customer_Name.Business_Name)
    
class Purchase_Payment_Report(models.Model):
    p_k=models.AutoField(primary_key=True)
    Reference_No=models.CharField(max_length=1000,null=True,blank=True)
    Paid_On=models.DateTimeField(auto_now_add=True)
    Amount=models.TextField(null=True,blank=True)
    Supplier=models.ForeignKey(Business_name,on_delete=models.CASCADE)
    Payment_Method=models.IntegerField(choices=PAYMENT_METHOD,default=0)
    Purchase=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return str(self.Reference_No)+' '+str(self.Supplier.Business_Name)
    
class Sell_Payment_Report(models.Model):
    p_k=models.AutoField(primary_key=True)
    Reference_No=models.CharField(max_length=1000,null=True,blank=True)
    Paid_On=models.DateTimeField(auto_now_add=True)
    Amount=models.TextField(null=True,blank=True)
    Customer=models.ForeignKey(Business_name,on_delete=models.CASCADE)
    Customer_group=models.ForeignKey(Customer_Group,on_delete=models.CASCADE)
    Payment_Method=models.IntegerField(choices=PAYMENT_METHOD,default=0)
    Sell=models.CharField(max_length=1000,null=True,blank=True)
    
    def __str__(self):
        return str(self.Reference_No)+' '+str(self.Customer.Business_Name)

class Expense_Categories_List(models.Model):
    p_k=models.AutoField(primary_key=True)
    Expense_Category_Name=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.Expense_Category_Name
    

class Expense_Report(models.Model):
    p_k=models.AutoField(primary_key=True)
    Expense_Categories=models.ForeignKey(Expense_Categories_List,on_delete=models.CASCADE)
    Total_Expense=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.Expense_Categories.Expense_Category_Name)+' '+str(self.Total_Expense)
    
class Register_Report(models.Model):
    p_k=models.AutoField(primary_key=True)
    Open_Time=models.DateTimeField(auto_now_add=True)
    Close_Time=models.DateTimeField(auto_now_add=True)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE)
    User=models.CharField(max_length=1000,null=True,blank=True) #Foreignkey User er
    Card_Slips=models.TextField(null=True,blank=True)
    Total_Cheques=models.TextField(null=True,blank=True)
    Total_Cash=models.TextField(null=True,blank=True)
    Bank_Transfer=models.TextField(null=True,blank=True)
    Advance_Payment=models.TextField(null=True,blank=True)
    Bkash_Nagad_Rocket_Upay=models.TextField(null=True,blank=True)
    Other_Payments=models.TextField(null=True,blank=True)
    Total=models.TextField(null=True,blank=True)
    Actions=models.IntegerField(choices=ACTION_STATUS,default=0)
    
    def __str__(self):
        return str(self.Location.Location)

class Sales_Report_Added(models.Model):
    p_k=models.AutoField(primary_key=True)
    Date=models.DateTimeField(auto_now_add=True)
    Invoice_No=models.TextField(null=True,blank=True)
    Customer_Name=models.ForeignKey(Business_name,on_delete=models.CASCADE)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE)
    Payment_Status=models.IntegerField(choices=PAYMENT_METHOD,default=0)
    Total_Amount=models.TextField(null=True,blank=True)
    Total_Paid=models.TextField(null=True,blank=True)
    Total_Remaining=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.Invoice_No)+' '+str(self.Location.Location)
    

class Sales_Report_With_Commission(models.Model):
    p_k=models.AutoField(primary_key=True)
    Date=models.DateTimeField(auto_now_add=True)
    Invoice_No=models.TextField(null=True,blank=True)
    Customer_Name=models.ForeignKey(Business_name,on_delete=models.CASCADE)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE)
    Payment_Status=models.IntegerField(choices=PAYMENT_METHOD,default=0)
    Total_Amount=models.TextField(null=True,blank=True)
    Total_Paid=models.TextField(null=True,blank=True)
    Total_Remaining=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.Invoice_No)+' '+str(self.Location.Location)
    
    
class Sales_Report_Expense(models.Model):
    p_k=models.AutoField(primary_key=True)
    Date=models.DateTimeField(auto_now_add=True)
    Reference_No=models.TextField(null=True,blank=True)
    Expense_Category=models.ForeignKey(Expense_Categories_List,on_delete=models.CASCADE)
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE)
    Payment_Status=models.IntegerField(choices=PAYMENT_METHOD,default=0)
    Total_Amount=models.TextField(null=True,blank=True)
    Expense_For=models.TextField(null=True,blank=True)
    Expense_Note=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.Reference_No)+' '+str(self.Location.Location)
    

class Stock_Report(models.Model):
    p_k=models.AutoField(primary_key=True)
    SKU=models.CharField(max_length=1000,null=True,blank=True) #Foreignkey use SKU er 
    Product=models.CharField(max_length=1000,null=True,blank=True) #Foreignkey Product er But kon field lagbe milaia,na lagle nai
    Variation=models.CharField(max_length=1000,null=True,blank=True)
    Category=models.CharField(max_length=1000,null=True,blank=True) #Foreignkey Category er
    Location=models.ForeignKey(Location_Set,on_delete=models.CASCADE)
    Unit_Selling_Price=models.TextField(null=True,blank=True)
    Current_Stock=models.TextField(null=True,blank=True)
    Current_Stock_Value_by_purchase_price=models.TextField(null=True,blank=True)
    Current_Stock_Value_by_sale_price=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.Product)+' '+str(self.Location.Location)
    

