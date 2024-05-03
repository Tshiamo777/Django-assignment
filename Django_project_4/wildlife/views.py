from django.db.models import Count, Sum, Q
from .models import Property, Province, Organisation, AnnualPopulation, Taxon, User

# 1. Show properties with type 'Private' and 'Community'
def get_private_community_properties():
    properties = Property.objects.filter(property_type__name__in=['Private', 'Community']).values()
    return list(properties)

# 2. Show provinces that have organisation or properties
def get_provinces_with_organisation_or_properties():
    provinces = Province.objects.filter(
        organisation__isnull=False
    ).distinct().values()

    provinces_with_properties = Province.objects.filter(
        property__isnull=False
    ).distinct().values()

    provinces = list(provinces) + list(provinces_with_properties)
    
    return provinces

# 3. Show organisation and property count for (2)
def get_organisation_property_count():
    organisations = Organisation.objects.annotate(property_count=Count('property')).values()
    return list(organisations)

# 4. Show the number of adult male and adult female of Acinonyx Jubatus, on all properties, on year 2021
def get_acinonyx_jubatus_population():
    acinonyx_jubatus_adult_male_count = AnnualPopulation.objects.filter(
        year=2021,
        taxon__scientific_name='Acinonyx Jubatus',
    ).aggregate(adult_male_count=Sum('adult_male'))

    acinonyx_jubatus_adult_female_count = AnnualPopulation.objects.filter(
        year=2021,
        taxon__scientific_name='Acinonyx Jubatus',
    ).aggregate(adult_female_count=Sum('adult_female'))

    return {
        'adult_male_count': acinonyx_jubatus_adult_male_count['adult_male_count'],
        'adult_female_count': acinonyx_jubatus_adult_female_count['adult_female_count']
    }

# 5. Show the number of species owned by Property 'Zakki Property'
def get_species_count_for_zakki_property():
    species_count = Property.objects.get(name='Zakki Property').annualpopulation_set.values('taxon').distinct().count()
    return {'species_count': species_count}

# 6. Show organisation with largest area available to species
def get_organisation_with_largest_area():
    organisation = Organisation.objects.annotate(
        total_area_available=Sum('property__annualpopulation__area_available_to_species')
    ).order_by('-total_area_available').first()
    return {'organisation': organisation.name}

# 7. Show property with the most varying species
def get_property_with_most_varying_species():
    property_with_most_species = Property.objects.annotate(
        species_count=Count('annualpopulation__taxon', distinct=True)
    ).order_by('-species_count').first()
    return {'property': property_with_most_species.name}

# 8. Show property with the most animal count
def get_property_with_most_animal_count():
    property_with_most_animals = Property.objects.annotate(
        total_animal_count=Sum('annualpopulation__total')
    ).order_by('-total_animal_count').first()
    return {'property': property_with_most_animals.name}

# 9. Show Province with highest adult male
def get_province_with_highest_adult_male():
    province = Province.objects.annotate(
        total_adult_male=Sum('property__annualpopulation__adult_male')
    ).order_by('-total_adult_male').first()
    return {'province': province.name}

# 10. Given 1 scientific name and rank, show parent and child taxon rank
def get_taxon_hierarchy(scientific_name):
    taxon = Taxon.objects.get(scientific_name=scientific_name)
    parent_taxon = taxon.parent
    child_taxon_rank = taxon.taxon_rank
    parent_taxon_rank = None
    if parent_taxon:
        parent_taxon_rank = parent_taxon.taxon_rank
    return {
        'parent_taxon_rank': str(parent_taxon_rank),
        'child_taxon_rank': str(child_taxon_rank)
    }

# 11. Show taxon without child
def get_taxon_without_child():
    taxon_without_child = Taxon.objects.filter(parent__isnull=True).values()
    return list(taxon_without_child)

# 12. Show user that adds most Annual Population records
def get_user_with_most_population_records():
    user_with_most_records = User.objects.annotate(
        population_record_count=Count('annualpopulation')
    ).order_by('-population_record_count').first()
    return {'user': user_with_most_records.username}