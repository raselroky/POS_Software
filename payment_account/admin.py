from django.contrib import admin
from .models import List_Account,Account_type,Liability,Assets,Trial_Balance,Cash_Flow,Payment_Account_Report

class List_Account_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Name','Account_Type','Account_Number','Note','Balance','Account_Details','Added_By','Action')
admin.site.register(List_Account,List_Account_Column_Display)

class Account_type_Column_Display(admin.ModelAdmin):
    list_display=('p_k','account_type')
admin.site.register(Account_type,Account_type_Column_Display)

class Liability_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Liability_Name','Total_Liability')
admin.site.register(Liability,Liability_Column_Display)

class Assets_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Asset_Name','Total_Assets')
admin.site.register(Assets,Assets_Column_Display)

class Trial_Balance_Column(admin.ModelAdmin):
    list_display=('p_k','Trial_Balance_Name','Debit','Credit')
admin.site.register(Trial_Balance,Trial_Balance_Column)

class Cash_Flow_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Date','Account','Description','Payment_Method','Payment_Details','Debit','Credit','Total_Balance')
admin.site.register(Cash_Flow,Cash_Flow_Column_Display)

class Payment_Account_Report_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Date','Payment_Reference_No','Invoice_Or_Reference_No','Amount','Payment_Type','Description','Action')
admin.site.register(Payment_Account_Report,Payment_Account_Report_Column_Display)