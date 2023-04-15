"""
URL configuration for ABlueRainbowProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from a_blue_rainbow import views


urlpatterns = [
    # HOME
    path("", views.home_view, name="home-view"),

    # ASSISTED LIVING
    path("assistedliving/", views.alf_search_view),
    path("assistedliving/list", views.assistedliving_list_view),
    # path("assistedliving/create", views.alf_create_view),
    path("assistedliving/details/<int:id>", views.alf_detail_view),
    path("assistedliving/update/<int:id>", views.alf_update_view,
         name="alf-update-view"),
    path("assistedliving/delete/<int:id>", views.alf_delete_view,
         name="alf-delete-view"),

    # HOME HEALTH
    path("homehealth/", views.hhc_search_view),
    path("homehealth/list", views.homehealth_list_view),
    # path("homehealth/create", views.hhc_create_view),
    path("homehealth/details/<int:id>", views.hhc_detail_view),
    path("homehealth/update/<int:id>", views.hhc_update_view,
         name="hhc-update-view"),
    path("homehealth/delete/<int:id>", views.hhc_delete_view,
         name="hhc-delete-view"),

    # SKILLED NURSING
    path("skillednursing/list", views.skillednursing_list_view),
    # path("skillednursing/create", views.snf_create_view),
    path("skillednursing/details/<int:id>", views.snf_detail_view),
    path("skillednursing/update/<int:id>", views.snf_update_view,
         name="snf-update-view"),
    path("skillednursing/delete/<int:id>", views.snf_delete_view,
         name="snf-delete-view"),

    # HOSPICE
    path("hospice/", views.hospice_search_view),
    path("hospice/list", views.hospice_list_view),
    path("hospice/create", views.hospice_create_view),
    path("hospice/details/<int:id>", views.hospice_detail_view),
    path("hospice/update/<int:id>", views.hospice_update_view,
         name="hospice-update-view"),
    path("hospice/delete/<int:id>", views.hospice_delete_view,
         name="hospice-delete-view"),

    path("feedback/", views.userfeedback_create_view),
    path("search_facilities", views.search_facilities, name="search-facilities"),
    path("admin/", admin.site.urls),
    # path('api/', include('a_blue_rainbow.urls')),
]
