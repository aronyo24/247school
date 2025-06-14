from django.contrib import admin
from .models import Visitor


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = (
        'ip_address',
        'private_ip',
        'user_agent',
        'city',
        'country',
        'last_visit',
        'visit_count',
    )
    list_filter = ('country', 'city', 'last_visit')  # Sidebar filters
    search_fields = ('ip_address', 'user_agent', 'city', 'country')  # Top search
    ordering = ('-last_visit',)  # Most recent first
    readonly_fields = ('last_visit', 'visit_count')  # These are auto-updated

    fieldsets = (
        (None, {
            'fields': ('ip_address', 'private_ip', 'user_agent')
        }),
        ('Location Information', {
            'fields': ('city', 'country'),
        }),
        ('Visit Details', {
            'fields': ('visit_count', 'last_visit'),
        }),
    )

    def has_add_permission(self, request):
        # Disallow adding visitors manually from the admin panel
        return False
