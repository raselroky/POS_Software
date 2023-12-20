from django.contrib import admin
from .models import All_Reports

class All_Reports_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Total_Products_Item','Total_Purchase','Total_Sell_Return','Total_Customer_Due','Total_Supplier_Due','Total_Customer_Opening_Balance_Due','Total_Supplier_Opening_Balance_Due')
admin.site.register(All_Reports,All_Reports_Column_Display)
