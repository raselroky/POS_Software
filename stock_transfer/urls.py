from django.urls import path,include
from . import views

urlpatterns = [
    path('stocktransferl/',views.Stock_Transfer_Api_List.as_view()),
    path('stocktransferd/<int:pk>',views.Stock_Transfer_Api_Detail.as_view()),
    path('stocktransferfilter/',views.Stock_Transfer_Search_Api.as_view()),
]
