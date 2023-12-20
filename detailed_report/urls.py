from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('expensecategoriesl/',views.Expense_Categories_List_Api_List.as_view()),
    path('expensecategoriesld/<int:pk>',views.Expense_Categories_List_Api_Detail.as_view()),

    #purchase and sale report
    path('purchaseapil/',views.Purchases_Api_List.as_view()),
    path('purchaseapid/<int:pk>',views.Purchases_Api_Detail.as_view()),

    path('salesapil/',views.Sales_Api_List.as_view()),
    path('salesapid/<int:pk>',views.Sales_Api_Detail.as_view()),

    path('salepurchaseapil/',views.Sale_Purchase_Api_List.as_view()),
    path('salepurchaseapid/<int:pk>',views.Sale_Purchase_Api_Detail.as_view()),

    path('dueamountapil/',views.Due_Amount_Api_List.as_view()),
    path('dueamountapid/<int:pk>',views.Due_Amount_Api_Detail.as_view()),

    #tax report
    path('inputtaxapil/',views.Input_Tax_Api_List.as_view()),
    path('inputtaxapid/<int:pk>',views.Input_Tax_Api_Detail.as_view()),

    path('outputtaxapil/',views.Output_Tax_Api_List.as_view()),
    path('outputtaxapid/<int:pk>',views.Output_Tax_Api_Detail.as_view()),

    path('expensetaxapil/',views.Expense_Tax_Api_List.as_view()),
    path('expensetaxapid/<int:pk>',views.Expense_Tax_Api_Detail.as_view()),

    #supplier and customer report
    path('supplierandcustomerapil/',views.Supplier_And_Customer_Report_Api_List.as_view()),
    path('supplierandcustomerapid/<int:pk>',views.Supplier_And_Customer_Report_Api_Detail.as_view()),

    #customer group report
    path('customergroupapil/',views.Customer_Group_Report_Api_List.as_view()),
    path('customergroupapid/<int:pk>',views.Customer_Group_Report_Api_Detail.as_view()),

    #stock adjustment report
    path('stockadjustmentreportapil/',views.Stock_Adjustment_Report_Api_List.as_view()),
    path('stockadjustmentreportapid/<int:pk>',views.Stock_Adjustment_Report_Api_Detail.as_view()),

    #item report
    path('itemreportapil/',views.Item_Report_Api_List.as_view()),
    path('itemreportapid/<int:pk>',views.Item_Report_Api_Detail.as_view()),

    #product purchase report
    path('productpurchasereportapil/',views.Product_Purchase_Report_Api_List.as_view()),
    path('productpurchasereportapid/<int:pk>',views.Product_Purchase_Report_Api_Detail.as_view()),

    #product sell report
    path('productsellreportapil/',views.Product_Sell_Report_Api_List.as_view()),
    path('productsellreportapid/<int:pk>',views.Product_Sell_Report_Api_Detail.as_view()),

    #purchase payment report
    path('purchasepaymentreportapil/',views.Purchase_Payment_Report_Api_List.as_view()),
    path('purchasepaymentreportapid/<int:pk>',views.Purchase_Payment_Report_Api_Detail.as_view()),

    #sell payment report
    path('sellpaymentreportapil/',views.Sell_Payment_Report_Api_List.as_view()),
    path('sellpaymentreportapid/<int:pk>',views.Sell_Payment_Report_Api_Detail.as_view()),

    #expense report 
    path('expensereportapil/',views.Expense_Report_Api_List.as_view()),
    path('expensereportapid/<int:pk>',views.Expense_Report_Api_Detail.as_view()),

    #register report
    path('registerreportapil/',views.Register_Report_Api_List.as_view()),
    path('registerreportapid/<int:pk>',views.Register_Report_Api_Detail.as_view()),

    #sales representative report
    path('salesreportaddedapil/',views.Sales_Report_Added_Api_List.as_view()),
    path('salesreportaddedapid/<int:pk>',views.Sales_Report_Added_Api_Detail.as_view()),

    path('salesreportwithcommisionapil/',views.Sales_Report_With_Commission_Api_List.as_view()),
    path('salesreportwithcommisionapid/<int:pk>',views.Sales_Report_With_Commission_Api_Detail.as_view()),

    path('salesreportexpenseapil/',views.Sales_Report_Expense_Api_List.as_view()),
    path('salesreportexpenseapid/<int:pk>',views.Sales_Report_Expense_Api_Detail.as_view()),

    #stock report
    path('stockreportapil/',views.Stock_Report_Api_List.as_view()),
    path('stockreportapid/<int:pk>',views.Stock_Report_Api_Detail.as_view()),
]
