from django.contrib import admin
from .models import All_Number,All_Number_Sms,All_Supplier_Number,All_Supplier_Number_Smss,All_Customer_Number,All_Customer_Number_Smss

class All_Number_Column_Display(admin.ModelAdmin):
    list_display=('p_k','Number')
admin.site.register(All_Number,All_Number_Column_Display)

class All_Number_Sms_Column_Display(admin.ModelAdmin):
    list_display=('p_k','sms','get_numbers')

    def get_numbers(self, obj):
        if obj.numbers.all():
            return list(obj.numbers.all().values_list('name', flat=True))
        else:
            return 'NA'
admin.site.register(All_Number_Sms,All_Number_Sms_Column_Display)


class All_Supplier_Number_Column_Display(admin.ModelAdmin):
    list_display=('p_k','number')
admin.site.register(All_Supplier_Number,All_Supplier_Number_Column_Display)

class All_Supplier_Number_Sms_Column_Display(admin.ModelAdmin):
    list_display=('p_k','sms','get_numbers')

    def get_numbers(self, obj):
        if obj.numbers.all():
            return list(obj.numbers.all().values_list('name', flat=True))
        else:
            return 'NA'
admin.site.register(All_Supplier_Number_Smss,All_Supplier_Number_Sms_Column_Display)


class All_Customer_Number_Column_Display(admin.ModelAdmin):
    list_display=('p_k','number')
admin.site.register(All_Customer_Number,All_Customer_Number_Column_Display)

class All_Customer_Number_Sms_Column_Display(admin.ModelAdmin):
    list_display=('p_k','sms','get_numbers')

    def get_numbers(self, obj):
        if obj.numbers.all():
            return list(obj.numbers.all().values_list('name', flat=True))
        else:
            return 'NA'
admin.site.register(All_Customer_Number_Smss,All_Customer_Number_Sms_Column_Display)