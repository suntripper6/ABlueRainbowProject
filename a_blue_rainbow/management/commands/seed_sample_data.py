from django.core.management.base import BaseCommand

from a_blue_rainbow.models import (
    AssistedLivingFacility,
    HomeHealthFacility,
    HospiceFacility,
    Provider,
    SkilledNursingFacility,
    State,
    UserFeedback,
)


class Command(BaseCommand):
    help = "Load idempotent sample data for local development."

    def handle(self, *args, **options):
        provider_specs = [
            {
                "facility_type": "Assisted Living",
                "facility_name": "Rainbow Assisted Living Network",
            },
            {
                "facility_type": "Home Health",
                "facility_name": "Rainbow Home Health Network",
            },
            {
                "facility_type": "Hospice",
                "facility_name": "Rainbow Hospice Network",
            },
            {
                "facility_type": "Skilled Nursing",
                "facility_name": "Rainbow Skilled Nursing Network",
            },
        ]

        providers = {}
        for provider_spec in provider_specs:
            provider, _ = Provider.objects.update_or_create(
                facility_type=provider_spec["facility_type"],
                defaults={"facility_name": provider_spec["facility_name"]},
            )
            providers[provider_spec["facility_type"]] = provider

        State.objects.update_or_create(
            zip_code=34221,
            defaults={
                "latitude": 27.5231,
                "longitude": -82.5723,
                "city": "Palmetto",
                "state": "Florida",
                "zcta": True,
                "parent_zcta": "34221",
                "population": 21931,
                "density": 1438.6,
                "county_fips": 81,
                "county_name": "Manatee",
                "county_weights": "100",
                "county_names_all": "Manatee",
                "county_fips_all": "081",
                "imprecise": False,
                "military": False,
                "timezone": "America/New_York",
                "state_abbrev": "FL",
            },
        )

        AssistedLivingFacility.objects.update_or_create(
            name="Sunrise Harbor Assisted Living",
            address="101 Bayview Drive",
            defaults={
                "facility_type": providers["Assisted Living"],
                "city": "Palmetto",
                "state": "FL",
                "zip_code": "34221",
                "phone_number": "9415550101",
                "medicare_elig": True,
                "map": "https://maps.example.com/sunrise-harbor",
                "rating": 4,
                "reviews": "Warm staff and a strong activity calendar.",
                "official_website": "https://example.com/sunrise-harbor",
                "transportation_services": True,
                "case_management": True,
            },
        )

        HomeHealthFacility.objects.update_or_create(
            name="Coastal Care Home Health",
            address="202 River Road",
            defaults={
                "facility_type": providers["Home Health"],
                "city": "Bradenton",
                "state": "FL",
                "zip_code": "34205",
                "phone_number": "9415550102",
                "medicare_elig": True,
                "map": "https://maps.example.com/coastal-care",
                "rating": 5,
                "reviews": "Responsive nursing visits and therapy scheduling.",
                "official_website": "https://example.com/coastal-care",
                "private_duty_aide": True,
                "private_duty_nurse": True,
                "skilled_therapy": True,
                "transportation_services": True,
                "case_management": True,
            },
        )

        HospiceFacility.objects.update_or_create(
            name="Harbor Light Hospice",
            address="303 Sunset Lane",
            defaults={
                "facility_type": providers["Hospice"],
                "city": "Sarasota",
                "state": "FL",
                "zip_code": "34236",
                "phone_number": "9415550103",
                "medicare_elig": True,
                "map": "https://maps.example.com/harbor-light",
                "rating": 5,
                "reviews": "Strong caregiver communication and grief support.",
                "official_website": "https://example.com/harbor-light",
            },
        )

        SkilledNursingFacility.objects.update_or_create(
            name="Gulfside Skilled Nursing Center",
            address="404 Magnolia Avenue",
            defaults={
                "facility_type": providers["Skilled Nursing"],
                "city": "Bradenton",
                "state": "FL",
                "zip_code": "34208",
                "phone_number": "9415550104",
                "medicare_elig": True,
                "map": "https://maps.example.com/gulfside-skilled-nursing",
                "rating": 4,
                "reviews": "Reliable rehab staff and discharge planning.",
                "official_website": "https://example.com/gulfside-skilled-nursing",
                "transportation_services": True,
                "case_management": True,
            },
        )

        UserFeedback.objects.update_or_create(
            email="caregiver@example.com",
            defaults={
                "name": "Jordan Rivers",
                "comments": "The provider search made comparing care options much easier.",
            },
        )

        self.stdout.write(self.style.SUCCESS("Sample data loaded."))