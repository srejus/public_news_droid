from django.contrib import admin
from .models import *

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','posted_by','is_fake','created_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['news','commented_by','comment','created_at']

admin.site.register(News,NewsAdmin)
admin.site.register(Comment,CommentAdmin)

