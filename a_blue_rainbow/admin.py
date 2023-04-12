from django.contrib import admin
from .models import UserFeedback, HomeHealthFacilities, AssistedLivingFacilities, SkilledNursingFacilities, \
    HospiceFacilities, Providers, States
# Register your models here.
admin.site.register(UserFeedback)
admin.site.register(Providers)
admin.site.register(States)


class FacilityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'city', 'state', 'zip_code']
    search_fields = ['name', 'state']


admin.site.register(AssistedLivingFacilities, FacilityAdmin)
admin.site.register(HomeHealthFacilities, FacilityAdmin)
admin.site.register(SkilledNursingFacilities, FacilityAdmin)
admin.site.register(HospiceFacilities, FacilityAdmin)
