from django.core.management.base import BaseCommand
from a_blue_rainbow.models import State, AssistedLivingFacility, HomeHealthFacility, HospiceFacility, SkilledNursingFacility, Provider

class Command(BaseCommand):
    help = 'Seeds sample data for testing'

    def handle(self, *args, **kwargs):
        # Create Providers
        al_prov, _ = Provider.objects.get_or_create(id=1, defaults={'facility_type': 'Assisted Living', 'facility_name': 'Assisted Living Provider'})
        hh_prov, _ = Provider.objects.get_or_create(id=2, defaults={'facility_type': 'Home Health', 'facility_name': 'Home Health Provider'})
        hosp_prov, _ = Provider.objects.get_or_create(id=3, defaults={'facility_type': 'Hospice', 'facility_name': 'Hospice Provider'})
        snf_prov, _ = Provider.objects.get_or_create(id=4, defaults={'facility_type': 'Skilled Nursing', 'facility_name': 'Skilled Nursing Provider'})

        for i in range(1, 15):
            AssistedLivingFacility.objects.get_or_create(
                name=f"Golden Years {i}",
                address=f"{123 + i} Sunset Blvd",
                city="Los Angeles",
                state="CA",
                zip_code=f"9000{i % 10}",
                phone_number=f"555-01{i:02d}",
                facility_type=al_prov
            )
        
        # Home Health
        HomeHealthFacility.objects.get_or_create(
            name="Care at Home",
            address="456 Hill St",
            city="San Francisco",
            state="CA",
            zip_code="94101",
            phone_number="555-0102",
            facility_type=hh_prov
        )
        
        # Hospice
        HospiceFacility.objects.get_or_create(
            name="Peaceful Journey",
            address="789 Valley Ln",
            city="San Diego",
            state="CA",
            zip_code="92101",
            phone_number="555-0103",
            facility_type=hosp_prov
        )
        
        # Skilled Nursing
        SkilledNursingFacility.objects.get_or_create(
            name="Recovery Center",
            address="321 Oak Way",
            city="Sacramento",
            state="CA",
            zip_code="95814",
            phone_number="555-0104",
            facility_type=snf_prov
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded sample data'))
