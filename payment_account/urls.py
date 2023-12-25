from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('listaccountapil/',views.List_Account_Api_List.as_view()),
    path('listaccountapid/<int:pk>',views.List_Account_Api_Detial.as_view()),
    path('listaccountfilter/',views.List_Account_Search_Api.as_view()),

    path('acccounttypel/',views.Account_Types_Api_List.as_view()),
    path('acccounttyped/<int:pk>',views.Account_Types_Api_Detail.as_view()),
    path('acccounttypefilter/',views.Account_Type_Search_Api.as_view()),

    path('liabilityapil/',views.Liability_Api_List.as_view()),
    path('liabilityapid/<int:pk>',views.Liability_Api_Detail.as_view()),
    path('liabilityfilter/',views.Liability_Search_Api.as_view()),

    path('assetsapil/',views.Assets_Api_List.as_view()),
    path('assetsapid/<int:pk>',views.Assets_Api_Detail.as_view()),
    path('assetsfilter/',views.Assets_Search_Api.as_view()),

    path('trialbalanceapil/',views.Trial_Balance_Api_List.as_view()),
    path('trialbalanceapid/<int:pk>',views.Trial_Balance_Api_Detail.as_view()),
    path('trialbalancefilter/',views.Trial_Balance_Search_Api.as_view()),

    path('cashflowapil/',views.Cash_Flow_Api_List.as_view()),
    path('cashflowapid/<int:pk>',views.Cash_Flow_Api_Detail.as_view()),
    path('cashflowfilter/',views.Cash_Flow_Search_Api.as_view()),

    path('paymentaccountreportapil/',views.Payment_Account_Report_Api_List.as_view()),
    path('paymentaccountreportapid/<int:pk>',views.Payment_Account_Report_Api_Detail.as_view()),
    path('paymentaccountreportfilter/',views.Payment_Account_Report_Api_List.as_view()),

    
]
