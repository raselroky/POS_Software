from django.contrib import admin
from .models import AddProduct,Brand,Category,Warranty,Unit,SubCategory,OpeningStock








class Brand_Column_Display(admin.ModelAdmin):
    list_display=field_names = (
    'brand_name',
    'short_description',
)
admin.site.register(Brand,Brand_Column_Display)



class Category_Column_Display(admin.ModelAdmin):
    list_display=field_names = (
    'category_name',
    'category_code',
    'description',
    'brand',  
)
admin.site.register(Category,Category_Column_Display)

class Subcategory_Column_Display(admin.ModelAdmin):
    list_display=field_names = (
    'category',
    'subcategory_name', 
)
admin.site.register(SubCategory,Subcategory_Column_Display)


class Warranty_Column_Display(admin.ModelAdmin):
    list_display=field_names = (
    'warranty_name',
    'warranty_description',
    'warranty_duration',
    'warranty_duration_type', 
)
admin.site.register(Warranty,Warranty_Column_Display)


class Unit_Column_Display(admin.ModelAdmin):
    list_display=field_names = (
    'unit_name',
    'unit_short_name',
    'allow_decimal', 
)
admin.site.register(Unit,Unit_Column_Display)






class OpeningStock_Column_Display(admin.ModelAdmin):
    list_display=field_names = (
    'sku',
    'location',
    'quantity',
    'unit_cost_before_tax',
    'lot_number',
    'expiry_date',

)
admin.site.register(OpeningStock,OpeningStock_Column_Display)





class AddProduct_Column_Display(admin.ModelAdmin):
    list_display=field_names = (
    'product_name',
    'sku',
    'unit',
    'brand',
    'category',
    'subcategory',
    'warranty',
    'business_locations',
    'alert_quantity',
    # 'barcode_type',
    # 'manage_stock',
    # 'expires_in',
    # 'expiry_period_unit'
)
admin.site.register(AddProduct,AddProduct_Column_Display)
