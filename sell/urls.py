from django.urls import path,include
from . import views

urlpatterns = [
    path('allsalesapil/',views.All_Sales_Api_List.as_view()),
    path('allsalesapid/<int:pk>',views.All_Sales_Api_Detail.as_view()),
    path('allsalesfilterapi/',views.All_Sales_Searh_Api.as_view()),


    path('listdraftapil/',views.List_Draft_Api_List.as_view()),
    path('listdraftapid/<int:pk>',views.List_Draft_Api_Detail.as_view()),
    path('listdraftfilter/',views.List_Draft_Searh_Api.as_view()),

    path('listsellreturnapil/',views.List_Sell_Return_Api_List.as_view()),
    path('listsellreturnapid/<int:pk>',views.List_Sell_Return_Api_Detail.as_view()),
    path('listsellreturnfilter/',views.List_Sell_Return_Searh_Api.as_view()),

    path('shipmentapil/',views.Shipments_Api_List.as_view()),
    path('shipmentapid/<int:pk>',views.Shipments_Api_Detail.as_view()),
    path('shipmentfilter/',views.Shipment_Searh_Api.as_view()),

    path('discountapil/',views.Discount_Api_List.as_view()),
    path('discountapid/<int:pk>',views.Discount_Api_Detail.as_view()),
    path('discountfilter/',views.Discount_Searh_Api.as_view()),

    path('locationapil/',views.Location_Set_Api_List.as_view()),
    path('locationapid/<int:pk>',views.Location_Set_Api_Detail.as_view()),
    path('locationfilter/',views.Location_Search_Api.as_view()),

    
]