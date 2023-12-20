from django.urls import path
from .views import (
    BrandList, BrandDetail,
    CategoryList, CategoryDetail,
    SubCategoryList, SubCategoryDetail,
    WarrantyList, WarrantyDetail,
    UnitList, UnitDetail,
    AddProductList, AddProductDetail,
    OpeningStockList, OpeningStockDetail,VariationsListCreateView, VariationsRetrieveUpdateDestroyView
)
from .views import BarcodeGenerator

urlpatterns = [
    path('brands/', BrandList.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandDetail.as_view(), name='brand-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('subcategories/', SubCategoryList.as_view(), name='subcategory-list'),
    path('subcategories/<int:pk>/', SubCategoryDetail.as_view(), name='subcategory-detail'),
    path('warranties/', WarrantyList.as_view(), name='warranty-list'),
    path('warranties/<int:pk>/', WarrantyDetail.as_view(), name='warranty-detail'),
    path('units/', UnitList.as_view(), name='unit-list'),
    path('units/<int:pk>/', UnitDetail.as_view(), name='unit-detail'),
    path('addproducts/', AddProductList.as_view(), name='addproduct-list'),
    path('addproducts/<int:pk>/', AddProductDetail.as_view(), name='addproduct-detail'),
    path('variations/', VariationsListCreateView.as_view(), name='variations-list-create'),
    path('variations/<int:pk>/', VariationsRetrieveUpdateDestroyView.as_view(), name='variations-detail'),
    path('openingstocks/', OpeningStockList.as_view(), name='openingstock-list'),
    path('openingstocks/<int:pk>/', OpeningStockDetail.as_view(), name='openingstock-detail'),
    path('generate-barcode/', BarcodeGenerator.as_view(), name='generate-barcode')
]
