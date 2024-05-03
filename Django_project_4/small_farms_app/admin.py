from django.contrib.gis import admin
from .models import InfrustructureItem, InfrustructureType, ManagmentLog, LogAction

# Register your models here.
from django.contrib.gis import forms
from django.contrib.gis.admin import GISModelAdmin
from django.contrib.gis.forms.widgets import OSMWidget

class BaseOSMAdmin(GISModelAdmin):
    formfield_overrides = {
        forms.PointField: {"widget": OSMWidget},
    }

class InfrustructureItemAdmin(BaseOSMAdmin):
    list_display = ['name', 'notes','geometry','infrustructure_item_type']
    search_fields = ['name', 'notes','geometry','infrustructure_item_type']
    list_filter = ['name']

class InfrustructureTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'notes', 'image']
    search_fields = ['name', 'notes', 'image']
    list_filter = ['name']

class ManagmentLogAdmin(admin.ModelAdmin):
    list_display = ['name', 'notes', 'condition', 'infrustructure_item', 'infrustructure_log_action']
    search_fields = ['name', 'notes', 'condition', 'infrustructure_item', 'infrustructure_log_action']
    list_filter = ['condition']

class LogActionAdmin(admin.ModelAdmin):
    list_display = ['name', 'notes', 'sort_order']
    search_fields = ['name', 'notes', 'sort_order']


admin.site.register(InfrustructureItem, InfrustructureItemAdmin)
admin.site.register(InfrustructureType, InfrustructureTypeAdmin)
admin.site.register(ManagmentLog, ManagmentLogAdmin)
admin.site.register(LogAction, LogActionAdmin)