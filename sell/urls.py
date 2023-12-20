from django.urls import path,include
from . import views

urlpatterns = [
    path('allsalesapil/',views.All_Sales_Api_List.as_view()),
    path('allsalesapid/<int:pk>',views.All_Sales_Api_Detail.as_view()),


    path('listdraftapil/',views.List_Draft_Api_List.as_view()),
    path('listdraftapid/<int:pk>',views.List_Draft_Api_Detail.as_view()),

    path('listsellreturnapil/',views.List_Sell_Return_Api_List.as_view()),
    path('listsellreturnapid/<int:pk>',views.List_Sell_Return_Api_Detail.as_view()),

    path('shipmentapil/',views.Shipments_Api_List.as_view()),
    path('shipmentapid/<int:pk>',views.Shipments_Api_Detail.as_view()),

    path('discountapil/',views.Discount_Api_List.as_view()),
    path('discountapid/<int:pk>',views.Discount_Api_Detail.as_view()),

    path('locationapil/',views.Location_Set_Api_List.as_view()),
    path('locationapid/<int:pk>',views.Location_Set_Api_Detail.as_view()),

    path('allsalesfilterapi/',views.All_Sales_Filter_Api.as_view()),
]