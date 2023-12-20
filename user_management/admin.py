# in user_management/admin.py
from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'first_name', 'last_name', 'is_active', 'is_staff','mobile_number','position','image')

admin.site.register(CustomUser, CustomUserAdmin)
