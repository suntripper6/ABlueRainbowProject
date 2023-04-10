from django.db import models


# Create your models here.
class UserFeedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comments = models.TextField()

    def __str__(self):
        return self.name


class States(models.Model):
    zip = models.IntegerField(null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    city = models.CharField(max_length=50, null=True)
    state_name = models.CharField(max_length=50, null=True)
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
        return self.state_abbrev, self.state_name, self.county_name, self.city, self.zip


class Providers(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class HospiceFacilities(models.Model):
    type = models.ForeignKey(
        Providers, on_delete=models.CASCADE, related_name='hospice')
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    state_name = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    medicare_elig = models.BooleanField(default=True)
    map = models.TextField()
    rating = models.IntegerField()
    reviews = models.TextField()
    official_website = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SkilledNursingFacilities(models.Model):
    type = models.ForeignKey(
        Providers, on_delete=models.CASCADE, related_name='skilled_nursing')
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    state_name = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    medicare_elig = models.BooleanField(default=True)
    transportation_services = models.BooleanField(default=True)
    case_management = models.BooleanField(default=True)
    map = models.TextField()
    rating = models.IntegerField()
    reviews = models.TextField()
    official_website = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AssistedLivingFacilities(models.Model):
    type = models.ForeignKey(
        Providers, on_delete=models.CASCADE, related_name='assisted_living')
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    state_name = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    medicare_elig = models.BooleanField(default=True)
    transportation_services = models.BooleanField(default=True)
    case_management = models.BooleanField(default=True)
    map = models.TextField()
    rating = models.IntegerField()
    reviews = models.TextField()
    official_website = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class HomeHealthFacilities(models.Model):
    type = models.ForeignKey(
        Providers, on_delete=models.CASCADE, related_name='home_health')
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    state_name = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    medicare_elig = models.BooleanField(default=True)
    private_duty_aide = models.BooleanField(default=True)
    private_duty_nurse = models.BooleanField(default=True)
    skilled_therapy = models.BooleanField(default=True)
    transportation_services = models.BooleanField(default=True)
    case_management = models.BooleanField(default=True)
    map = models.TextField()
    rating = models.IntegerField()
    reviews = models.TextField()
    official_website = models.CharField(max_length=255)

    def __str__(self):
        return self.name
