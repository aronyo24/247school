from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email')
    search_fields = ('name', 'position', 'email')
