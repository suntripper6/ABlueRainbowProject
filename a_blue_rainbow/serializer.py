from rest_framework import serializers

from .models import UserFeedback, Providers, HomeHealthFacilities, AssistedLivingFacilities, SkilledNursingFacilities, \
    HospiceFacilities, States


class UserFeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFeedback
        fields = ('id', 'name', 'email', 'comments')


class HomeHealthFacilitiesSerializer(serializers.ModelSerializer):
    provider = serializers.HyperlinkedRelatedField(
        view_name='provider_detail',
        many=True,
        read_only=True
    )

    state = serializers.HyperlinkedRelatedField(
        view_name='state_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = HomeHealthFacilities
        fields = ('id', 'name', 'address', 'city', 'state', 'zip_code', 'phone_number',
                  'type_id', 'medicare_elig', 'private_duty_aide', 'private_duty_nurse',
                  'skilled_therapy', 'transportation_services', 'case_management', 'map',
                  'rating', 'reviews', 'official_website', 'provider', 'state')


class AssistedLivingFacilitiesSerializer(serializers.ModelSerializer):
    provider = serializers.HyperlinkedRelatedField(
        view_name='provider_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = AssistedLivingFacilities
        fields = ('id', 'name', 'address', 'city', 'state', 'zip_code', 'phone_number',
                  'type_id', 'medicare_elig', 'skilled_therapy', 'transportation_services', 'case_management',
                  'map', 'rating', 'reviews', 'official_website', 'provider')


class SkilledNursingFacilitiesSerializer(serializers.ModelSerializer):
    provider = serializers.HyperlinkedRelatedField(
        view_name='provider_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = SkilledNursingFacilities
        fields = ('id', 'name', 'address', 'city', 'state', 'zip_code', 'phone_number',
                  'type_id', 'medicare_elig', 'transportation_services', 'case_management',
                  'map', 'rating', 'reviews', 'official_website', 'provider')


class HospiceFacilitiesSerializer(serializers.ModelSerializer):
    provider = serializers.HyperlinkedRelatedField(
        view_name='provider_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = HospiceFacilities
        fields = ('id', 'name', 'address', 'city', 'state', 'zip_code', 'phone_number',
                  'type_id', 'medicare_elig', 'map', 'rating', 'reviews', 'official_website', 'provider')


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Providers
        # fields = ('id', 'home_health', 'assisted_living', 'skilled_nursing', 'hospice')
        fields = ('id', 'type')


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ('id', 'zip_code', 'latitude', 'longitude', 'city', 'state', 'zcta', 'parent_zcta', 'population',
                  'density', 'county_fips', 'county_name', 'county_weights', 'county_names_all',
                  'county_fips_all', 'imprecise', 'military', 'timezone', 'state_id')


