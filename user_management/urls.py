
from django.urls import path
from .import views

urlpatterns = [
    path('usersapil/',views.User_Api_List.as_view()),
    path('usersapid/<int:pk>', views.User_Api_Detail.as_view()),

    path('loginapi/',views.Login_Api.as_view()),
    
    
]
