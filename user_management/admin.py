# in user_management/admin.py
from django.contrib import admin
from .models import CustomUser,Roles,Sales_Commission_Ager,Adds

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'first_name', 'last_name', 'is_active', 'is_staff','mobile_number','position','image','Role','Sales_Commission_Percentage','Max_Sales_Discount_Percentage','contact','Date_Of_Birth','Gender','Marital_Status','Blood_Group','Phone_Number','Alternate_Contact_Number','Family_Contact_Number','Facebook_Link','Twitter_Link','Permanent_Address','Current_Address','Account_Holders_Name','Account_Number','Bank_Name','Bank_Identifier_Code','Branch','Tax_Payer_ID','Basic_Salary','Basic_Salary','Pay_Term','Pay_Components')
admin.site.register(CustomUser, CustomUserAdmin)

class Roles_Column_Display(admin.ModelAdmin):
    list_display=('id','Role')

admin.site.register(Roles,Roles_Column_Display)

class Sales_Commission_Ager_Column_Display(admin.ModelAdmin):
    list_display=('id','Name','Email','Contact_Number','Address','Sales_Commission_Percentage','Action')
admin.site.register(Sales_Commission_Ager,Sales_Commission_Ager_Column_Display)

class Adds_Colum_Display(admin.ModelAdmin):
    list_display=('id','Prefix','First_Name','Last_Name','Email','Contact_Number','Address','Sales_Commission_Percentage')
admin.site.register(Adds,Adds_Colum_Display)


