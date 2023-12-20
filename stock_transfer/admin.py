from django.contrib import admin
from .models import Stock_Transfer

class Stock_Transfer_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Date','Reference_No','Location_From','Location_To','Status','Shipping_Charges','Total_Amount','Additional_Notes')
admin.site.register(Stock_Transfer,Stock_Transfer_Column_Display)