from django.urls import path,include
from . import views

urlpatterns = [
    path('stockadjustmentapil/',views.Stock_Adjustment_Api_List.as_view()),
    path('stockadjustmentapid/<int:pk>',views.Stock_Adjustment_Api_Detail.as_view()),
]
