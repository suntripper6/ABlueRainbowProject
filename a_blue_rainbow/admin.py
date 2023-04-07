from django.contrib import admin
from .models import UserFeedback, HomeHealthFacilities, AssistedLivingFacilities, SkilledNursingFacilities, \
    HospiceFacilities, Providers, States, ZipCodes
# Register your models here.
admin.site.register(UserFeedback)
admin.site.register(HomeHealthFacilities)
admin.site.register(AssistedLivingFacilities)
admin.site.register(SkilledNursingFacilities)
admin.site.register(HospiceFacilities)
admin.site.register(Providers)
admin.site.register(States)
admin.site.register(ZipCodes)
