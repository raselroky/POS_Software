# urls.py
from django.urls import path
from .views import (
    ExpenseCategoryListCreateView,
    ExpenseCategoryDetailView,
    ExpenseSubcategoryListCreateView,
    ExpenseSubcategoryDetailView,

)
from .views import ExpenseListCreateView, ExpenseDetailView

urlpatterns = [
    path('expense-categories/', ExpenseCategoryListCreateView.as_view(), name='expense-category-list-create'),
    path('expense-categories/<int:pk>/', ExpenseCategoryDetailView.as_view(), name='expense-category-detail'),
    path('expense-subcategories/', ExpenseSubcategoryListCreateView.as_view(), name='expense-subcategory-list-create'),
    path('expense-subcategories/<int:pk>/', ExpenseSubcategoryDetailView.as_view(), name='expense-subcategory-detail'),

    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),


]
