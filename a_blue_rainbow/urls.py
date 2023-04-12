from django.contrib import admin
from django .urls import path, include
from .import views


urlpatterns = [
    path("", views.home_view),
    path("hospice", views.hospice_view),
    path('userfeedback', views.UserFeedBackListView.as_view(),
         name='user_feedback_list'),
    path('userfeedback/details/<int:pk>',
         views.UserFeedBackDetailView.as_view(), name='user_feedback_detail'),
    path('providers', views.ProviderListView.as_view(), name='provider_list'),
    path('provider/details/<int:pk>',
         views.ProviderDetailView.as_view(), name='provider_detail'),
    # path('hospice', views.HospiceListView.as_view(), name='hospice_list'),
    # path('hospice/details/<int:pk>',
    #      views.HospiceDetailView.as_view(), name='hospice_detail'),
    path('skillednursing', views.SkilledNursingListView.as_view(),
         name='skilled_nursing_list'),
    path('skillednursing/details/<int:pk>',
         views.SkilledNursingDetailView.as_view(), name='skilled_nursing_detail'),
    path('assistedliving', views.AssistedLivingListView.as_view(),
         name='assisted_living_list'),
    path('assistedliving/details/<int:pk>',
         views.AssistedLivingDetailView.as_view(), name='assisted_living_detail'),
    path('homehealth', views.HomeHealthListView.as_view(), name='home_health_list'),
    path('homehealth/details/<int:pk>',
         views.HomeHealthDetailView.as_view(), name='home_health_detail'),
    path('states', views.StateListView.as_view(), name='state_list'),
    path('states/details/<int:pk>',
         views.StateDetailView.as_view(), name='state_detail'),
]
