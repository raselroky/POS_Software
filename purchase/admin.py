from django.contrib import admin
from .models import Purchases,List_Purchase_Return,Add_Purchase

class Purchases_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Created_At','Reference_No','Location','Supplier','Purchase_Status','Payment_Status','Grand_Total','Payment_Due','Added_By')
admin.site.register(Purchases,Purchases_Column_Display)

class Add_Purchase_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Supplier','Reference_No','Purchase_Date','Purchase_Status','Address','Business_Location','Pay_Term','Attached_Document')
admin.site.register(Add_Purchase,Add_Purchase_Column_Display)

class List_Purchase_Return_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Created_At','Reference_No','Parent_Purchase','Location','Supplier','Payment_Status','Grand_Total','Payment_Due')
admin.site.register(List_Purchase_Return,List_Purchase_Return_Column_Display)