from django.contrib import admin
from .models import Account
# Register your models here.
@admin.register(Account)
class AccountModelAdmin(admin.ModelAdmin):
    list_display=('user','is_active','first_name','degree',)
    list_editable=('is_active','first_name','degree')
    
    
    # list_filter=('user','username','is_active','first_name','degree')

