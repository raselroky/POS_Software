
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('reportapi/',views.All_Reports_Api.as_view()),
]