# admin.py
from django.contrib import admin
from .models import ExpenseCategory, ExpenseSubcategory
from .models import Expense, Payment



admin.site.register(ExpenseCategory)
admin.site.register(ExpenseSubcategory)
admin.site.register(Expense)
admin.site.register(Payment)