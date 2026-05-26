from django.urls import path

from . import views


urlpatterns = [
    path("feedback/", views.UserFeedbackListView.as_view(), name="user_feedback_list"),
    path("feedback/<int:pk>/", views.UserFeedbackDetailView.as_view(), name="user_feedback_detail"),
    path("providers/", views.ProviderListView.as_view(), name="provider_list"),
    path("providers/<int:pk>/", views.ProviderDetailView.as_view(), name="provider_detail"),
    path("states/", views.StateListView.as_view(), name="state_list"),
    path("states/<int:pk>/", views.StateDetailView.as_view(), name="state_detail"),
    path("assistedliving/", views.AssistedLivingListView.as_view(), name="assisted_living_list"),
    path("assistedliving/<int:pk>/", views.AssistedLivingDetailView.as_view(), name="assisted_living_detail"),
    path("homehealth/", views.HomeHealthListView.as_view(), name="home_health_list"),
    path("homehealth/<int:pk>/", views.HomeHealthDetailView.as_view(), name="home_health_detail"),
    path("skillednursing/", views.SkilledNursingListView.as_view(), name="skilled_nursing_list"),
    path("skillednursing/<int:pk>/", views.SkilledNursingDetailView.as_view(), name="skilled_nursing_detail"),
    path("hospice/", views.HospiceListView.as_view(), name="hospice_list"),
    path("hospice/<int:pk>/", views.HospiceDetailView.as_view(), name="hospice_detail"),
]
