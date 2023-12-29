from django.urls import path,include
from . import views

urlpatterns = [
    path('allsalesadd/',views.All_Sales_Add_Api.as_view()),
    path('allsalesapid/<int:pk>',views.All_Sales_Api_Detail.as_view()),
    path('allsalesdisplayfilter/',views.All_Sales_All_Show_Searh_Api.as_view()),


    path('listdraftadd/',views.List_Draft_Add_Api.as_view()),
    path('listdraftapid/<int:pk>',views.List_Draft_Api_Detail.as_view()),
    path('listdraftdisplayfilter/',views.List_Draft_All_Show_Searh_Api.as_view()),

    path('listsellreturnadd/',views.List_Sell_Return_Add_Api.as_view()),
    path('listsellreturnapid/<int:pk>',views.List_Sell_Return_Api_Detail.as_view()),
    path('listsellreturndisplayfilter/',views.List_Sell_Return_All_Show_Searh_Api.as_view()),

    path('shipmentadd/',views.Shipment_Add_Api.as_view()),
    path('shipmentapid/<int:pk>',views.Shipments_Api_Detail.as_view()),
    path('shipmentdisplayfilter/',views.Shipment_All_Show_Searh_Api.as_view()),

    path('discountadd/',views.Discount_Add_Api.as_view()),
    path('discountapid/<int:pk>',views.Discount_Api_Detail.as_view()),
    path('discountdisplayfilter/',views.Discount_All_Show_Searh_Api.as_view()),

    path('locationapil/',views.Location_Set_Api_List.as_view()),
    path('locationapid/<int:pk>',views.Location_Set_Api_Detail.as_view()),
    path('locationfilter/',views.Location_Search_Api.as_view()),

    path('filterapil/',views.Filter_Add_Search_Api.as_view()),
    path('filterapid/<int:pk>',views.Filter_Api_Detail.as_view()),
    
]