from django.contrib import admin
from .models import All_Sales,List_Draft,Shipments,Discount,Location_Set,List_Sell_Return,Filter

class Location_Set_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Location',)
admin.site.register(Location_Set,Location_Set_Column_Display)

class All_Sales_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Created_At','Invoice_No','Customer_Name','Contact_Number','Location','Payment_Status','Payment_Method','Total_Amount','Total_Paid','Sell_Due','Sell_Return_Due','Shipping_Status','Shipping_Address','Total_Items','Added_By')
admin.site.register(All_Sales,All_Sales_Column_Display)

class List_Draft_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Created_At','Reference_No','Customer_Name','Contact_Number','Location','Total_Items','Added_By')
admin.site.register(List_Draft,List_Draft_Column_Display)

class List_Sell_Return_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Created_At','Invoice_No','Parent_Sale','Customer_Name','Contact_Number','Location','Payment_Status','Total_Amount','Payment_Due')
admin.site.register(List_Sell_Return,List_Sell_Return_Column_Display)

class Shipments_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Created_At','Invoice_No','Customer_Name','Contact_Number','Location','Shipping_Status','Payment_Status','Service_Staff')
admin.site.register(Shipments,Shipments_Column_Display)

class Discount_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Name','Starts_At','Ends_At','Discount_Amount','Priority','Brand','Category','Product','Location')
admin.site.register(Discount,Discount_Column_Display)

class Filter_Column_Display(admin.ModelAdmin):
    list_display=('Business_Location','Customer','Payment_Status','Date_Range','User','Sales_Commission_Agent','Shipping_Status')
admin.site.register(Filter,Filter_Column_Display)