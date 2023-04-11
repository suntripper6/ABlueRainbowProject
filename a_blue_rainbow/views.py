from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from rest_framework import generics
from rest_framework.views import APIView
from .serializer import UserFeedBackSerializer, HomeHealthFacilitiesSerializer, AssistedLivingFacilitiesSerializer, \
    SkilledNursingFacilitiesSerializer, HospiceFacilitiesSerializer, StateSerializer, ProviderSerializer
from .models import UserFeedback, HomeHealthFacilities, AssistedLivingFacilities, SkilledNursingFacilities, \
    HospiceFacilities, States, Providers


# PROVIDER VIEW (FOR NOW)
def home_view(request):
    provider_obj = Providers.objects.get(id=2)
    provider_qs = Providers.objects.all()

    context = {
        "id": provider_obj.id,
        "type": provider_obj.type,
        "provider_qs": provider_qs,
    }

    HTML_STRING = render_to_string("provider-view.html", context=context)
    # HTML_STRING = """<h1>{type} (id: {id})</h1>""".format(**context)

    return HttpResponse(HTML_STRING)


# HOSPICE VIEW (FOR NOW)
def hospice_view(request):
    hospice_obj = HospiceFacilities.objects.get(id=2)
    hospice_qs = HospiceFacilities.objects.all()

    context = {
        "id": hospice_obj.id,
        "type": hospice_obj.type,
        "hospice_qs": hospice_qs,
    }

    HTML_STRING = render_to_string("hospice-view.html", context=context)
    # HTML_STRING = """<h1>{type} (id: {id})</h1>""".format(**context)

    return HttpResponse(HTML_STRING)


class UserFeedBackListView(generics.ListCreateAPIView):
    queryset = UserFeedback.objects.all()
    serializer_class = UserFeedBackSerializer


class UserFeedBackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserFeedback.objects.all()
    serializer_class = UserFeedBackSerializer


class HomeHealthListView(generics.ListCreateAPIView):
    queryset = HomeHealthFacilities.objects.all()
    serializer_class = HomeHealthFacilitiesSerializer


class HomeHealthDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomeHealthFacilities.objects.all()
    serializer_class = HomeHealthFacilitiesSerializer


class AssistedLivingListView(generics.ListCreateAPIView):
    queryset = AssistedLivingFacilities.objects.all()
    serializer_class = AssistedLivingFacilitiesSerializer


class AssistedLivingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AssistedLivingFacilities.objects.all()
    serializer_class = AssistedLivingFacilitiesSerializer


class SkilledNursingListView(generics.ListCreateAPIView):
    queryset = SkilledNursingFacilities.objects.all()
    serializer_class = SkilledNursingFacilitiesSerializer


class SkilledNursingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SkilledNursingFacilities.objects.all()
    serializer_class = SkilledNursingFacilitiesSerializer


class HospiceListView(generics.ListCreateAPIView):
    queryset = HospiceFacilities.objects.all()
    serializer_class = HospiceFacilitiesSerializer

    # context = {
    #     "query": queryset,
    # }

    # HTML_STRING = render_to_string("hospice-view.html", context=context)


class HospiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HospiceFacilities.objects.all()
    serializer_class = HospiceFacilitiesSerializer


class StateListView(generics.ListCreateAPIView):
    queryset = States.objects.all()
    serializer_class = StateSerializer


class StateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = States.objects.all()
    serializer_class = StateSerializer


class ProviderListView(generics.ListCreateAPIView):
    queryset = Providers.objects.all()
    serializer_class = ProviderSerializer


class ProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Providers.objects.all()
    serializer_class = ProviderSerializer
