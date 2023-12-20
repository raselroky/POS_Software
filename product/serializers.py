from rest_framework import serializers
from .models import AddProduct,Brand,Category,Warranty,Unit,SubCategory,OpeningStock,Variations
from . import generator

class Brand_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields=('__all__')


class Category_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields=('__all__')


class SubCategory_Serializer(serializers.ModelSerializer):
    # category = Category_Serializer()
    class Meta:
        model=SubCategory
        fields=('__all__')

class Warranty_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Warranty
        fields=('__all__')


class Unit_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Unit
        fields=('__all__')


class VariationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variations
        fields = '__all__'


class OpeningStock_Serializer(serializers.ModelSerializer):
    class Meta:
        model=OpeningStock
        fields=('__all__')



class AddProduct_Serializer(serializers.ModelSerializer):
    # brand = serializers.CharField(write_only=True)
    # category = serializers.CharField(write_only=True)
    # subcategory = serializers.CharField(write_only=True)
    
    # unit = Unit_Serializer()
    # warranty = Warranty_Serializer()
    # product_variation = ProductVariationValue_Serializer()
    class Meta:
        model = AddProduct
        fields = '__all__'

    # def create(self, validated_data):
    #     brand_name = validated_data.pop('brand')
    #     category_name = validated_data.pop('category')
    #     subcategory_name = validated_data.pop('subcategory')

    #     try:
    #         sku = validated_data['sku']
    #     except:
    #         sku = generator.generate_sku()
    #     brand, created = Brand.objects.get_or_create(brand_name=brand_name)
    #     category, created = Category.objects.get_or_create(
    #         category_name=category_name,
    #         brand = brand
    #     )

    #     subcategory, created = SubCategory.objects.get_or_create(
    #         subcategory_name=subcategory_name,
    #         category=category
    #     )

    #     validated_data['brand'] = brand
    #     validated_data['category'] = category
    #     validated_data['subcategory'] = subcategory
    #     validated_data['sku'] = sku

    #     return AddProduct.objects.create(**validated_data)
