from rest_framework import serializers

from .models import UserFeedback, Providers, HomeHealthFacilities, AssistedLivingFacilities, SkilledNursingFacilities, \
    HospiceFacilities, States, ZipCodes


class UserFeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFeedback
        fields = ('id', 'name', 'email', 'comments')


class HomeHealthFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeHealthFacilities
        fields = ('id', 'name', 'address', 'city', 'state', 'zip_code', 'phone_number',
                  'type', 'medicare_elig', 'private_duty_aide', 'private_duty_nurse',
                  'skilled_therapy', 'transportation_services', 'case_management', 'map',
                  'rating', 'reviews', 'official_website')


class AssistedLivingFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssistedLivingFacilities
        fields = ('id', 'name', 'address', 'city', 'state', 'zip_code', 'phone_number',
                  'type', 'medicare_elig', 'skilled_therapy', 'transportation_services', 'case_management',
                  'map', 'rating', 'reviews', 'official_website')


class SkilledNursingFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkilledNursingFacilities
        fields = ('id', 'name', 'address', 'city', 'state', 'zip_code', 'phone_number',
                  'type', 'medicare_elig', 'skilled_therapy', 'transportation_services', 'case_management',
                  'map', 'rating', 'reviews', 'official_website')


class HospiceFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospiceFacilities
        fields = ('id', 'name', 'address', 'city', 'state', 'zip_code', 'phone_number',
                  'type', 'medicare_elig', 'map', 'rating', 'reviews', 'official_website')


class ProviderSerializer(serializers.ModelSerializer):
    home_health = serializers.HyperlinkedRelatedField(
        view_name='home_health_detail',
        many=True,
        read_only=True
    )

    assisted_living = serializers.HyperlinkedRelatedField(
        view_name='assisted_living_detail',
        many=True,
        read_only=True
    )

    skilled_nursing = serializers.HyperlinkedRelatedField(
        view_name='skilled_nursing_detail',
        many=True,
        read_only=True
    )

    hospice = serializers.HyperlinkedRelatedField(
        view_name='hospice_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Providers
        fields = ('id', 'home_health', 'assisted_living', 'skilled_nursing', 'hospice')


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ('id', 'state', 'provider')


class ZipCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZipCodes
        fields = ('id', 'zip_code', 'state')
