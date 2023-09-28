from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', # Divide os dados dos contatos
    ordering = 'id', # Exibe o id de cada contato
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name' # Cria um icone d busca 
    list_per_page = 10
    list_max_show_all = 200
    # list_editable = 'first_name', 'last_name',
    list_display_links = 'id', 'phone',