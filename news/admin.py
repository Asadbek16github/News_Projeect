from django.contrib import admin
from .models import News, Category

# Register your models here.

@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ['title', 'published_time', 'author', 'status']
    list_filter = ['status', 'published_time', 'created_time']
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title']
    date_hierarchy = 'published_time'
    

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'category']
