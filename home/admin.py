from django.contrib import admin
from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_title = 'Your Custom Title'  # Change this to your desired title
    site_header = 'Your Custom Header'  # Change this to your desired header text
    index_title = 'Your Custom Index Title'  # Change this to your desired index title

custom_admin_site = CustomAdminSite(name='customadmin')


admin.site.site_header = 'Public News Droid Admin'