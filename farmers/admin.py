from django.contrib import admin
from .models import Farmer

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ['name', 'id_number', 'phone_number', 'county', 'farm_name', 'animal_type', 'number_of_animals']
    list_filter = ['county', 'animal_type', 'registration_date']
    search_fields = ['name', 'id_number', 'phone_number', 'farm_name']
    readonly_fields = ['registration_date', 'updated_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'id_number', 'phone_number')
        }),
        ('Location Details', {
            'fields': ('county', 'sub_county', 'ward')
        }),
        ('Farm Information', {
            'fields': ('farm_name',)
        }),
        ('Livestock Details', {
            'fields': ('animal_type', 'number_of_animals', 'animal_age')
        }),
        ('System Information', {
            'fields': ('registration_date', 'updated_at'),
            'classes': ('collapse',)
        }),
    )