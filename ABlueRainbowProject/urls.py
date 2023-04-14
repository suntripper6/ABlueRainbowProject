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
    path("", views.home_view, name="home-view"),
    # ASSISTED LIVING
    path("assistedliving/", views.alf_search_view),
    path("assistedliving/details/<int:id>", views.alf_detail_view),
    path("assistedliving/update/<int:id>", views.alf_update_view,
         name="alf-update-view"),
    path("hospice/delete/<int:id>", views.alf_delete_view,
         name="alf-delete-view"),

    # HOME HEALTH
    # path("homehealthcare/details/<int:id>", views.hospice_view),\

    # SKILLED NURSING
    # path("skillednursing/details/<int:id>", views.hospice_view),

    # HOSPICE
    path("hospice/", views.hospice_search_view),
    path("hospice/create", views.hospice_create_view),
    path("hospice/details/<int:id>", views.hospice_detail_view),
    path("hospice/update/<int:id>", views.hospice_update_view,
         name="hospice-update-view"),
    path("hospice/delete/<int:id>", views.hospice_delete_view,
         name="hospice-delete-view"),

    path("feedback/", views.userfeedback_create_view),
    path("admin/", admin.site.urls),
    # path('api/', include('a_blue_rainbow.urls')),
]
