from django.contrib import admin
from contact import models
from import_export.admin import ImportExportModelAdmin


@admin.register(models.Contact)
class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'id',
        'first_name', 
        'last_name', 
        'phone', 
        'show',
    ]

    ordering = 'id',

    search_fields = [
        'id',
        'first_name',
        'last_name',
    ]

    list_per_page = 10
    
    list_max_show_all = 200

    list_editable = 'show',

    list_display_links = [
        'id',
        'phone',
    ]

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    ordering = '-id',