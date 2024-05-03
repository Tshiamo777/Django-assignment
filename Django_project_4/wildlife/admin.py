from django.contrib import admin
from .models import PropertyType, Province, Organisation, Property, TaxonRank, Taxon, AnnualPopulation

# Register your models here.

admin.site.register(PropertyType)
admin.site.register(Province)
admin.site.register(Organisation)
admin.site.register(Property)
admin.site.register(TaxonRank)
admin.site.register(Taxon)
admin.site.register(AnnualPopulation)