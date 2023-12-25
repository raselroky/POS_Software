from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('purchaseadd/',views.Purchase_Add_Api.as_view()),
    path('purchaseapid/<int:pk>',views.Purchase_Api_Detail.as_view()),
    path('purchasedisplayfilter/',views.Purchase_All_Show_Search_Api.as_view()),

    path('addpurchaseadd/',views.Add_Purchase_Add_Api.as_view()),
    path('addpurchaseapid/<int:pk>',views.Add_Purchase_Api_Detail.as_view()),
    path('addpurchasedisplayfilter/',views.Add_Purchase_All_Show_Search_Api.as_view()),

    path('listpurchasereturnadd/',views.List_Purchase_Return_Add_Api.as_view()),
    path('listpurchasereturnapid/<int:pk>',views.List_Purchase_Return_Api_Detail.as_view()),
    path('listpurchasereturndisplayfilter/',views.List_Purchase_Return_All_Show_Search_Api.as_view()),

    path('expenseaddandsearch/',views.Additional_Expense_Add_Search_APi.as_view()),
    path('expenseapid/<int:pk>',views.Additional_Expense_Api_Detail.as_view()),

    
]