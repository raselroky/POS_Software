from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('allsmsapi/',views.All_Number_Sms_Api.as_view()),
    path('suppliersmsapi/',views.All_Supplier_Number_Smss_Api.as_view()),
    path('customersmsapi/',views.All_Customer_Number_Smss_Api.as_view()),
]
