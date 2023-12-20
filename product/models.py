from django.db import models
from .defaultValue import DURATION_TYPE,DURATION_TYPE,ALLOW_DECIMAL,BARCODE_TYPES,MANAGE_STOCK_CHOICES,EXPIRY_PERIOD_UNIT_CHOICES,TAX_TYPE_CHOICES,PRODUCT_TYPE_CHOICES,APPLICABLE_TAX_CHOICES

# Brand Model
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    short_description = models.TextField()

    def __str__(self):
        return self.brand_name

# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_code = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name


# Sub-Category Model
class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory_name
    

# Warranty Model
class Warranty(models.Model):
    warranty_name = models.CharField(max_length=100)
    warranty_description = models.TextField(blank=True)
    warranty_duration = models.PositiveIntegerField(default=1)
    warranty_duration_type = models.IntegerField(choices=DURATION_TYPE, default=0)

    def __str__(self):
        return self.warranty_name


# Unit Model
class Unit(models.Model):
    unit_name = models.CharField(max_length=100)
    unit_short_name = models.CharField(max_length=100,blank=True)
    allow_decimal = models.IntegerField(choices=ALLOW_DECIMAL)

    def __str__(self):
        return self.unit_name





#variations Type
class Variations(models.Model):
    name = models.CharField(max_length=200)
    value = models.JSONField()

    def set_value(self, x):
        self.value = x if isinstance(x, list) else [x]

    def __str__(self):
        return self.name
   

#Stock
class OpeningStock(models.Model):
    sku = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255, blank=True)
    quantity = models.PositiveIntegerField()
    unit_cost_before_tax = models.DecimalField(max_digits=10, decimal_places=2)
    lot_number = models.CharField(max_length=255, blank=True)
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.sku

# Product Model
class AddProduct(models.Model):
    product_name = models.CharField(max_length=1000)
    sku = models.CharField(max_length=36, unique=True, editable=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True)
    variation = models.ForeignKey(Variations, on_delete=models.CASCADE, blank=True,null=True)#updated
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null = True)
    warranty = models.ForeignKey(Warranty, on_delete=models.CASCADE, blank=True,null=True)
    business_locations = models.CharField(max_length=1000)
    alert_quantity = models.PositiveIntegerField()
    manage_stock = models.IntegerField(choices=MANAGE_STOCK_CHOICES,default=0)
    
    
    exc_tax = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    inc_tax = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    margin_percentage = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    product_image = models.ImageField(upload_to='products/', null=True, blank=True)
    
    # barcode_type = models.IntegerField(choices=BARCODE_TYPES,default=0)
    # expires_in = models.PositiveIntegerField(null=True,blank=True)
    # expiry_period_unit = models.CharField(max_length=7,choices=EXPIRY_PERIOD_UNIT_CHOICES,null=True,blank=True)
    # product_variation =models.ForeignKey(ProductVariationValue, on_delete=models.CASCADE, blank=True, null=True) 

    def __str__(self):
        return f"{self.product_name} (brand: {self.brand})"


