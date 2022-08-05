from django.contrib import admin
from . models import *
# Register your models here.
@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'keyword', 'description', 'logo',  'banner','favicon', 'mobile', 'mobile2', 'address', 'email', 'website', 'copyright_year']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'message', 'email', 'created', 'cleared', 'admin_note', 'status']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'img']
