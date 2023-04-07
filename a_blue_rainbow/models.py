from django.db import models


# Create your models here.
class UserFeedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comments = models.TextField()

    def __str__(self):
        return self.name


class HospiceFacilities(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    type = models.CharField(max_length=10)
    medicare_elig = models.BooleanField(default=True)
    map = models.TextField()
    rating = models.IntegerField()
    reviews = models.TextField()
    official_website = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SkilledNursingFacilities(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    type = models.CharField(max_length=10)
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
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    type = models.CharField(max_length=10)
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
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    type = models.CharField(max_length=10)
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


class Providers(models.Model):
    home_health = models.ForeignKey(HomeHealthFacilities, on_delete=models.CASCADE,
                                    related_name='home_health')
    assisted_living = models.ForeignKey(AssistedLivingFacilities, on_delete=models.CASCADE,
                                        related_name='assisted_living')
    skilled_nursing = models.ForeignKey(SkilledNursingFacilities, on_delete=models.CASCADE,
                                        related_name='skilled_nursing')
    hospice = models.ForeignKey(HospiceFacilities, on_delete=models.CASCADE,
                                related_name='hospice')

    def __str__(self):
        return self.home_health.name, self.assisted_living.name, self.skilled_nursing.name, self.hospice.name


class States(models.Model):
    provider = models.ForeignKey(Providers, on_delete=models.CASCADE, related_name='state')
    state = models.CharField(max_length=255)

    def __str__(self):
        return self.state


class ZipCodes(models.Model):
    state = models.ForeignKey(States, on_delete=models.CASCADE, related_name='zip_code')
    zip_code = models.CharField(max_length=15)

    def __str__(self):
        return self.zip_code
