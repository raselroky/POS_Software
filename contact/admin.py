from django.contrib import admin
from .models import Suppliers,Customers,Customer_Group,Business_name,Contact_id


class Business_name_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Business_Name','Category')
admin.site.register(Business_name,Business_name_Column_Display)

class Suppliers_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Contact_ID','Business_Name','Name','Email','Address','Mobile','Tax_Number','Supplier_group','Pay_Term','Total_Amount','Advance_Amount','Due_Amount','Return_Due_Amount','Paid_Status','Created_At')
admin.site.register(Suppliers,Suppliers_Column_Display)


class Customers_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Contact_ID','Business_Name','Name','Email','Mobile','Delivery_Address','Home_Address','Tax_Number','Credit_limit','Reward_Point','Customer_group','Pay_Term','Opening_Balance','Advance_Balance','Total_Sale_Due','Total_Sell_Return_Due','Shipping_Address','Created_At')
admin.site.register(Customers,Customers_Column_Display)


class Customer_group_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Customer_Group_Name','Calculation_Percentage','Selling_Price_Group')
admin.site.register(Customer_Group,Customer_group_Column_Display)

class Contact_id_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Contact_Ids')
admin.site.register(Contact_id,Contact_id_Column_Display)