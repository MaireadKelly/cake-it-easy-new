from django.contrib import admin
from .models import Cake

# Register your models here.
@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'slug', 'created_at', 'updated_at', 'image')
    search_fields = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category', 'created_at')
    ordering = ('name',)
