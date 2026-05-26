from rest_framework import serializers

from .models import (
    AssistedLivingFacility,
    HomeHealthFacility,
    HospiceFacility,
    Provider,
    SkilledNursingFacility,
    State,
    UserFeedback,
)


FACILITY_BASE_FIELDS = (
    'id', 'name', 'address', 'city', 'state', 'zip_code', 'phone_number',
    'facility_type', 'medicare_elig', 'map', 'rating', 'reviews', 'official_website'
)


class UserFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFeedback
        fields = ('id', 'name', 'email', 'comments')


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = FACILITY_BASE_FIELDS


class HomeHealthFacilitySerializer(FacilitySerializer):
    class Meta:
        model = HomeHealthFacility
        fields = FACILITY_BASE_FIELDS + (
            'private_duty_aide', 'private_duty_nurse', 'skilled_therapy',
            'transportation_services', 'case_management'
        )


class AssistedLivingFacilitySerializer(FacilitySerializer):
    class Meta:
        model = AssistedLivingFacility
        fields = FACILITY_BASE_FIELDS + ('transportation_services', 'case_management')


class SkilledNursingFacilitySerializer(FacilitySerializer):
    class Meta:
        model = SkilledNursingFacility
        fields = FACILITY_BASE_FIELDS + ('transportation_services', 'case_management')


class HospiceFacilitySerializer(FacilitySerializer):
    class Meta:
        model = HospiceFacility
        fields = FACILITY_BASE_FIELDS


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('id', 'facility_type', 'facility_name')


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'zip_code', 'latitude', 'longitude', 'city', 'state', 'zcta', 'parent_zcta', 'population',
                  'density', 'county_fips', 'county_name', 'county_weights', 'county_names_all',
                  'county_fips_all', 'imprecise', 'military', 'timezone', 'state_abbrev')


