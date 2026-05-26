from django.contrib import admin
from .models import (
    AssistedLivingFacility,
    HomeHealthFacility,
    HospiceFacility,
    Provider,
    SkilledNursingFacility,
    State,
    UserFeedback,
)


admin.site.register(UserFeedback)
admin.site.register(Provider)
admin.site.register(State)


class FacilityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'city', 'state', 'zip_code']
    search_fields = ['name', 'state']


admin.site.register(AssistedLivingFacility, FacilityAdmin)
admin.site.register(HomeHealthFacility, FacilityAdmin)
admin.site.register(SkilledNursingFacility, FacilityAdmin)
admin.site.register(HospiceFacility, FacilityAdmin)
