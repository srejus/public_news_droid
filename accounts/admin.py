from django.contrib import admin
from .models import *

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user','full_name','email']


admin.site.register(Account,AccountAdmin)
