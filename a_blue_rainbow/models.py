from django.db import models


# Create your models here.
class UserFeedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comments = models.TextField()

    def __str__(self):
        return self.name


class Provider(models.Model):
    def __str__(self):
        return self.name


class State(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='state')
    state = models.CharField(max_length=255)

    def __str__(self):
        return self.state


class ZipCode(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='zip_code')
    zip_code = models.CharField(max_length=15)

    def __str__(self):
        return self.zip_code



class HospiceFacilities(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='hospice')
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
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='skilled_nursing')
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
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='assisted_living')
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
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='home_health')
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


