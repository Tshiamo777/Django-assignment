from django.contrib import admin
from wildlife.models import PropertyType, Province, Organisation, Property, TaxonRank, Taxon, AnnualPopulation

# Register your models here.

class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_code', 'national', 'province']
    search_fields = ['name', 'short_code']
    list_filter = ['national', 'province']

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_code', 'province', 'property_type', 'organisation']
    search_fields = ['name', 'short_code']
    list_filter = ['province', 'property_type', 'organisation']

class TaxonRankAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class TaxonAdmin(admin.ModelAdmin):
    list_display = ['scientific_name', 'common_name_varbatim', 'taxon_rank', 'parent']
    search_fields = ['scientific_name', 'common_name_varbatim']
    list_filter = ['taxon_rank', 'parent']

class AnnualPopulationAdmin(admin.ModelAdmin):
    list_display = ['year', 'total', 'adult_male', 'adult_female', 'juvenile_male', 'juvenile_female', 'note', 'user', 'taxon', 'property']
    search_fields = ['year', 'taxon__scientific_name', 'property__name']
    list_filter = ['year', 'taxon', 'property']



admin.site.register(PropertyType, PropertyTypeAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(TaxonRank, TaxonRankAdmin)
admin.site.register(Taxon, TaxonAdmin)
admin.site.register(AnnualPopulation, AnnualPopulationAdmin)