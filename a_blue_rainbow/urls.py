from django.contrib import admin
from django .urls import path, include
from .import views


urlpatterns = [
    path('feedback/', views.UserFeedBackListView.as_view()),
    path('hospice', views.HospiceListView.as_view(), name='hospice_list'),
    path('hospice/details/<int:pk>', views.HospiceDetailView.as_view(), name='hospice_detail'),
    path('skillednursing', views.SkilledNursingListView.as_view(), name='skilled_nursing_list'),
    path('skillednursing/details/<int:pk>', views.SkilledNursingDetailView.as_view(), name='skilled_nursing_detail'),
    path('assistedliving', views.AssistedLivingListView.as_view(), name='assisted_living_list'),
    path('assistedliving/details/<int:pk>', views.AssistedLivingDetailView.as_view(), name='assisted_living_detail'),
    path('homeheatlh', views.HomeHealthListView.as_view(), name='home_health_list'),
    path('homehealth/details/<int:pk>', views.HomeHealthDetailView.as_view(), name='home_health_detail'),
    path('state', views.StateListView.as_view(), name='state_list'),
    path('state/details/<int:pk>', views.StateDetailView.as_view(), name='state_detail'),
    path('zipcode', views.ZipCodeListView.as_view(), name='zip_code_list'),
    path('zipcode/details/<int:pk>', views.ZipCodeDetailView.as_view(), name='zip_code_detail'),
]