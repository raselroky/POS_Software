from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('actions/',views.Action_Api.as_view()),

    path('suppliersapil/',views.Suppliers_Api_List.as_view()), #listing (show all and create data )
    path('suppliersapid/<int:pk>/',views.Suppliers_Api_Detail.as_view()), #show pindivisual by pk and delete by pk url parameter
    
    path('customersapil/',views.Customers_Api_List.as_view()), #listing (show all and create data )
    path('customersapid/<int:pk>',views.Customers_Api_Detail.as_view()), #show pindivisual by pk and delete by pk url parameter


    path('customergroupapil/',views.Customer_Group_Api_List.as_view()),
    path('customergroupapid/<int:pk>',views.Customer_Group_Api_Detail.as_view()),


    path('businessnameapil/',views.Business_name_Api_List.as_view()),
    path('businessnameapid/<int:pk>',views.Business_name_Api_Detail.as_view()),

    
    path('contactidapil/',views.Contact_id_Api_List.as_view()),
    path('contactidapid/<int:pk>',views.Contact_id_Api_Detail.as_view()),

    path('customerapifilter/',views.Customer_Searh_Api.as_view()),
    path('supplierapifilter/',views.Supplier_Searh_Api.as_view()),
]

