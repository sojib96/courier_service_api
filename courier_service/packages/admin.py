from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'tracking_number', 'sender', 'recipient_name', 'status', 'created_at', 'deleted_at')
    search_fields = ('tracking_number', 'recipient_name', 'recipient_address')
    list_filter = ('status', 'created_at', 'deleted_at')
    readonly_fields = ('tracking_number', 'created_at', 'updated_at', 'deleted_at')

    def has_delete_permission(self, request, obj=None):
        return False  


