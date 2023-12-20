from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('purchaseapil/',views.Purchases_Api_List.as_view()),
    path('purchaseapid/<int:pk>',views.Purchase_Api_Detail.as_view()),

    path('addpurchaseapil/',views.Add_Purchases_Api_List.as_view()),
    path('addpurchaseapid/<int:pk>',views.Add_Purchase_Api_Detail.as_view()),

    path('listpurchasereturnapil/',views.List_Purchase_Return_Api_List.as_view()),
    path('listpurchasereturnapid/<int:pk>',views.List_Purchase_Return_Api_Detail.as_view()),

    path('purchasefilterapi/',views.Purchase_Filter_Api.as_view()),
]