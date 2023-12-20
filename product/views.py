



from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AddProduct, Brand, Category, Warranty, Unit, SubCategory, OpeningStock,Variations
from .serializers import AddProduct_Serializer, Brand_Serializer, Category_Serializer, Warranty_Serializer, Unit_Serializer, SubCategory_Serializer, OpeningStock_Serializer,VariationsSerializer
from rest_framework import status
from rest_framework import generics


class CustomListCreateAPIView(generics.ListCreateAPIView):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class BrandList(CustomListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = Brand_Serializer
    def get_queryset(self):
        brand_name = self.request.query_params.get("brand_name",'')
        if brand_name:
            return Brand.objects.filter(brand_name__icontains = brand_name)
        return Brand.objects.all()

# class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = Brand_Serializer

class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = Brand_Serializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Brand deleted successfully'}, status=status.HTTP_200_OK)
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CategoryList(CustomListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer
    def get_queryset(self):
        category_name = self.request.query_params.get('category_name','')
        if category_name:
            return Category.objects.filter(category_name__icontains=category_name)
        return Category.objects.all()

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer

class SubCategoryList(CustomListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategory_Serializer
    def get_queryset(self):
        subcategory_name = self.request.query_params.get('subcategory_name','')
        if subcategory_name:
            return SubCategory.objects.filter(subcategory_name__icontains=subcategory_name)
        return SubCategory.objects.all()

class SubCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategory_Serializer

class WarrantyList(CustomListCreateAPIView):
    queryset = Warranty.objects.all()
    serializer_class = Warranty_Serializer
    def get_queryset(self):
        warranty_name = self.request.query_params.get('warranty_name','')
        if warranty_name:
            return Warranty.objects.filter(warranty_name__icontains=warranty_name)
        return Warranty.objects.all()

class WarrantyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warranty.objects.all()
    serializer_class = Warranty_Serializer

class UnitList(CustomListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = Unit_Serializer
    def get_queryset(self):
        unit_name = self.request.query_params.get("unit_name",'')
        if unit_name:
            return Unit.objects.filter(unit_name__icontains=unit_name)
        return Unit.objects.all()

class UnitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = Unit_Serializer

class AddProductList(CustomListCreateAPIView):
    queryset = AddProduct.objects.all()
    serializer_class = AddProduct_Serializer
    def get_queryset(self):
        queryset = AddProduct.objects.all()

        # Filter by product_name
        product_name = self.request.query_params.get('product_name', '')
        if product_name:
            queryset = queryset.filter(product_name__icontains=product_name)

        # Filter by category
        category = self.request.query_params.get('category', '')
        if category:
            queryset = queryset.filter(category__name=category)

        # Filter by unit
        unit = self.request.query_params.get('unit', '')
        if unit:
            queryset = queryset.filter(unit__name=unit)

        # Filter by brand
        brand = self.request.query_params.get('brand', '')
        if brand:
            queryset = queryset.filter(brand__name=brand)

        # Filter by business_location
        business_location = self.request.query_params.get('business_location', '')
        if business_location:
            queryset = queryset.filter(business_locations__contains=business_location)

        return queryset


class AddProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AddProduct.objects.all()
    serializer_class = AddProduct_Serializer



class OpeningStockList(CustomListCreateAPIView):
    queryset = OpeningStock.objects.all()
    serializer_class = OpeningStock_Serializer

class OpeningStockDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OpeningStock.objects.all()
    serializer_class = OpeningStock_Serializer
    
    
class VariationsListCreateView(generics.ListCreateAPIView):
    queryset = Variations.objects.all()
    serializer_class = VariationsSerializer
    def get_queryset(self):
        variations_name = self.request.query_params.get('name','')
        if variations_name:
            return Variations.objects.filter(name__icontains=variations_name)
        return Variations.objects.all()

class VariationsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Variations.objects.all()
    serializer_class = VariationsSerializer
    
    
    
    
    
    
# barcode_generator/views.py

import os
from django.conf import settings
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from PIL import Image, ImageDraw, ImageFont
import barcode
from barcode.writer import ImageWriter
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime

@method_decorator(csrf_exempt, name='dispatch')
class BarcodeGenerator(APIView):
    def draw_border(self, image, border_color=(200, 200, 200), border_width=10, dash_length=10):
        draw = ImageDraw.Draw(image)

        for x in range(5, image.width, dash_length * 2):
            draw.line([(x, 0), (x + dash_length, 0)], fill=border_color, width=border_width)
            draw.line(
                [(x, image.height - border_width), (x + dash_length, image.height - border_width)],
                fill=border_color,
                width=border_width,
            )

        for y in range(5, image.height, dash_length * 2):
            draw.line([(0, y), (0, y + dash_length)], fill=border_color, width=border_width)
            draw.line(
                [(image.width - border_width, y), (image.width - border_width, y + dash_length)],
                fill=border_color,
                width=border_width,
            )

    def generate_barcode_image(self, barcode_data):
        barcode_image = barcode.Code128(barcode_data, writer=ImageWriter())
        barcode_image.save('barcode')
        barcode_img = Image.open('barcode.png')
        # resized_img = barcode_img.resize((250, 200))
        return barcode_img

    def post(self, request, *args, **kwargs):
        
        data = request.data
        
        product_id = data.get('product_id', None)
        include_product = data.get('include_product', False)
        include_business = data.get("include_business", False)
        include_variations = data.get("include_variations", False)
        include_price = data.get("include_price", False)
        include_pcaking_date = data.get("include_packing_date", False)
        packing_date = data.get('packing_date')
        label_no = data.get("label_no")
        

        if not product_id:
            return Response({'error': 'Product ID is required.'}, status=400)

        try:
            product = AddProduct.objects.get(id=product_id)
        except AddProduct.DoesNotExist:
            return Response({'error': 'Product not found.'}, status=404)
        
        
                # Extracting information from the product
        product_name = product.product_name if include_product else ''
        variations = product.variation if product.variation else ''
        price = product.selling_price
        business_name = product.brand.brand_name if product.brand else ''
        
        
        
        image = Image.new("RGB", (700, 600), "white")

        # Call the function to draw the border
        self.draw_border(image)
        font = ImageFont.truetype("product/times new roman bold.ttf", 45)


    


        separator = '\n' # Using an em space as a separator

        product_details = f"{'' if not include_business else business_name.capitalize() + separator}{'' if not include_product else product_name.capitalize() + separator}{'' if not include_variations else variations.name.capitalize() + ': ' + ' '.join(map(str, variations.value)) + separator}{'' if not include_price else 'Price: ' + str(price) + separator}{'' if not include_pcaking_date else packing_date}"


        draw = ImageDraw.Draw(image)
        draw.text((150, 40), product_details, font=font, fill="black",align='center')

        barcode_img = self.generate_barcode_image(product.sku)
        image.paste(barcode_img, (150, 300))
        
        
        
        IMAGENAME = f'product{product_id}BARCODE.png'
        media_root = settings.MEDIA_ROOT
        barcode_directory = os.path.join(media_root, 'barcode')
        image_path = os.path.join(barcode_directory, IMAGENAME)
        image.save(image_path)
        image_url = request.build_absolute_uri(os.path.join(settings.MEDIA_URL, 'barcode',IMAGENAME))
        
        
        repeated_urls = [image_url] * label_no

        # Include the repeated_urls in the response
        response_data = {
            'message': 'Image saved successfully.',
            'image_urls': repeated_urls
        }
        return Response(response_data)


