
from django.urls import path
from .import views

urlpatterns = [

    path('usersaddandfilter/',views.User_Add_Search_Api.as_view()),
    path('usersapid/<int:pk>', views.User_Api_Detail.as_view()),
    
    path('rolesadd/',views.Roles_Add_Search_Api.as_view()),
    path('rolesapid/<int:pk>',views.Roles_Api_Detail.as_view()),
    path('rolesdisplayfilter/',views.Roles_Show_Search_Api.as_view()),

    path('salescommisionapil/',views.Sales_Commission_Ager_Api_List.as_view()),
    path('salescommisionapid/<int:pk>',views.Sales_Commission_Ager_Api_Detail.as_view()),

    path('addsapil/',views.Adds_Api_List.as_view()),
    path('addsapid/<int:pk>',views.Adds_Api_Detail.as_view()),

    path('permission/',views.Permission_Show_Search_Api.as_view()),

    path('loginapi/',views.Login_Api.as_view()),
    
    
]
