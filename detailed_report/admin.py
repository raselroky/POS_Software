from django.contrib import admin
from .models import Purchases,Sales,Sale_Purchase,Due_Amount,Input_Tax,Output_Tax,Expense_Tax,Supplier_And_Customer_Report,Customer_Group_Report,Stock_Adjustment_Report,Item_Report,Product_Purchase_Report,Product_Sell_Report,Purchase_Payment_Report,Sell_Payment_Report,Expense_Report,Register_Report,Expense_Categories_List,Sales_Report_Added,Sales_Report_With_Commission,Sales_Report_Expense,Stock_Report

class Purchases_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Total_Purchase','Purchase_Including_Tax','Total_Purchase_Return_Including_Tax','Purchase_Deu')
admin.site.register(Purchases,Purchases_Column_Display)

class Sales_Column_Dsiplay(admin.ModelAdmin):
    list_display=('p_k','Total_Sale','Sale_Including_Tax','Total_Sell_Return_Including_Tax','sale_Due')
admin.site.register(Sales,Sales_Column_Dsiplay)

class Sale_Purchase_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Sale_purchase')
admin.site.register(Sale_Purchase,Sale_Purchase_Column_Display)

class Due_Amount_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Due_amount')
admin.site.register(Due_Amount,Due_Amount_Column_Display)

class Expense_Categories_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Expense_Category_Name')
admin.site.register(Expense_Categories_List,Expense_Categories_Column_Display)

class Input_Tax_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Date','Reference_No','Supplier','Tax_Number','Total_Amount','Payment_Method','Discount','Vat')
admin.site.register(Input_Tax,Input_Tax_Column_Display)

class Output_Tax_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Date','Invoice_No','Customer','Tax_Number','Total_Amount','Payment_Method','Discount','Vat')
admin.site.register(Output_Tax,Output_Tax_Column_Display)

class Expense_Tax_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Date','Invoice_No','Tax_Number','Total_Amount','Payment_Method','Vat')
admin.site.register(Expense_Tax,Expense_Tax_Column_Display)

class Supplier_And_Customer_Report_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Contact','Total_Purchase','Total_Purchase_Return','Total_Sale','Total_Sell_Return','Opening_Balance_Due','Due')
admin.site.register(Supplier_And_Customer_Report,Supplier_And_Customer_Report_Column_Display)

class Customer_Group_Report_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Customer_group','Total_Sale')
admin.site.register(Customer_Group_Report,Customer_Group_Report_Column_Display)

class Stock_Adjustment_Report_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Date','Reference_No','Location','Adjustment_Type','Total_Amount','Total_Amount_Recovered','Reason','Added_By')
admin.site.register(Stock_Adjustment_Report,Stock_Adjustment_Report_Column_Display)

class Item_Report_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Product','SKU','Description','Purchase_Date','Purchase','Lot_Number','Supplier','Purchase_Price','Sell_Date','Sale','Customer','Location','Sell_Quantity','Selling_Price','Subtotal')
admin.site.register(Item_Report,Item_Report_Column_Display)

class Product_Purchase_Report_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Product','SKU','Supplier','Reference_No','Date','Location','Quantity','Total_Unit_Adjusted','Unit_Purchase_Price','Subtotal')
admin.site.register(Product_Purchase_Report,Product_Purchase_Report_Column_Display)

class Product_Sell_Report_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Product','SKU','Customer_Name','Contact_Id','Invoice_No','Date','Quantity','Unit_Price','Discount','Tax','Price_Inc_Tax','Total')
admin.site.register(Product_Sell_Report,Product_Sell_Report_Column_Display)

class Purchase_Payment_Report_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Reference_No','Paid_On','Amount','Supplier','Payment_Method','Purchase')
admin.site.register(Purchase_Payment_Report,Purchase_Payment_Report_Column_Display)

class Sell_Payment_Report_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Reference_No','Paid_On','Amount','Customer','Customer_group','Payment_Method','Sell')
admin.site.register(Sell_Payment_Report,Sell_Payment_Report_Column_Display)

class Expense_Report_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Expense_Categories','Total_Expense')
admin.site.register(Expense_Report,Expense_Report_Column_Display)

class Register_Report_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Open_Time','Close_Time','Location','User','Card_Slips','Total_Cheques','Total_Cash','Bank_Transfer','Advance_Payment','Bkash_Nagad_Rocket_Upay','Other_Payments','Total','Actions')
admin.site.register(Register_Report,Register_Report_Column_Display)

class Sales_Report_Added_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Date','Invoice_No','Customer_Name','Location','Payment_Status','Total_Amount','Total_Paid','Total_Remaining')
admin.site.register(Sales_Report_Added,Sales_Report_Added_Column_Display)

class Sales_Report_With_Commission_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Date','Invoice_No','Customer_Name','Location','Payment_Status','Total_Amount','Total_Paid','Total_Remaining')
admin.site.register(Sales_Report_With_Commission,Sales_Report_With_Commission_Column_Display)

class Sales_Report_Expense_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Date','Reference_No','Expense_Category','Location','Payment_Status','Total_Amount','Expense_For','Expense_Note')
admin.site.register(Sales_Report_Expense,Sales_Report_Expense_Column_Display)

class Stock_Report_Colum_Display(admin.ModelAdmin):
    list_display=('p_k','SKU','Product','Variation','Category','Location','Unit_Selling_Price','Current_Stock','Current_Stock_Value_by_purchase_price','Current_Stock_Value_by_sale_price')
admin.site.register(Stock_Report,Stock_Report_Colum_Display)
