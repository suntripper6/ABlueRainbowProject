from django.db import models


# Create your models here.
class UserFeedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comments = models.TextField()

    def __str__(self):
        return self.name


class States(models.Model):
    zip_code = models.IntegerField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zcta = models.BooleanField(null=True)
    parent_zcta = models.CharField(max_length=50, null=True)
    population = models.IntegerField(null=True)
    density = models.FloatField(null=True)
    county_fips = models.IntegerField(null=True)
    county_name = models.CharField(max_length=50, null=True)
    county_weights = models.CharField(max_length=128, null=True)
    county_names_all = models.CharField(max_length=64, null=True)
    county_fips_all = models.CharField(max_length=50, null=True)
    imprecise = models.BooleanField(null=True)
    military = models.BooleanField(null=True)
    timezone = models.CharField(max_length=50, null=True)
    state_abbrev = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.state, self.state_abbrev, self.county_name, self.city


class Providers(models.Model):
    facility_type = models.CharField(max_length=50)
    facility_name = models.CharField(max_length=255)

    def __str__(self):
        return self.facility_type


class HospiceFacilities(models.Model):
    facility_type = models.ForeignKey(
        Providers, on_delete=models.CASCADE, related_name='hospice', default=3)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15, null=True)
    medicare_elig = models.BooleanField(default=True, null=True)
    map = models.TextField(null=True)
    rating = models.IntegerField(null=True)
    reviews = models.TextField(null=True)
    official_website = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class SkilledNursingFacilities(models.Model):
    facility_type = models.ForeignKey(
        Providers, on_delete=models.CASCADE, related_name='skilled_nursing', default=4)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15, null=True)
    medicare_elig = models.BooleanField(default=True, null=True)
    transportation_services = models.BooleanField(default=True, null=True)
    case_management = models.BooleanField(default=True, null=True)
    map = models.TextField(null=True)
    rating = models.IntegerField(null=True)
    reviews = models.TextField(null=True)
    official_website = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class AssistedLivingFacilities(models.Model):
    facility_type = models.ForeignKey(
        Providers, on_delete=models.CASCADE, related_name='assisted_living', default=1)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15, null=True)
    medicare_elig = models.BooleanField(default=True, null=True)
    transportation_services = models.BooleanField(default=True, null=True)
    case_management = models.BooleanField(default=True, null=True)
    map = models.TextField(null=True)
    rating = models.IntegerField(null=True)
    reviews = models.TextField(null=True)
    official_website = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class HomeHealthFacilities(models.Model):
    facility_type = models.ForeignKey(
        Providers, on_delete=models.CASCADE, related_name='home_health', default=2)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15, null=True)
    medicare_elig = models.BooleanField(default=True, null=True)
    private_duty_aide = models.BooleanField(default=True, null=True)
    private_duty_nurse = models.BooleanField(default=True, null=True)
    skilled_therapy = models.BooleanField(default=True, null=True)
    transportation_services = models.BooleanField(default=True, null=True)
    case_management = models.BooleanField(default=True, null=True)
    map = models.TextField(null=True)
    rating = models.IntegerField(null=True)
    reviews = models.TextField(null=True)
    official_website = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
