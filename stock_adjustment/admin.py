from django.contrib import admin
from .models import Stock_Adjustment

class Stock_Adjustment_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Action','Date','Reference_No','Location','Adjustment_Type','Total_Amount','Total_Amount_Recovered','Reason','Added_By')
admin.site.register(Stock_Adjustment,Stock_Adjustment_Column_Display)

