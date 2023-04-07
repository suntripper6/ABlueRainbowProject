from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializer import UserFeedBackSerializer, HomeHealthFacilitiesSerializer, AssistedLivingFacilitiesSerializer, \
    SkilledNursingFacilitiesSerializer, HospiceFacilitiesSerializer, StateSerializer, ZipCodeSerializer
from .models import UserFeedback, HomeHealthFacilities, AssistedLivingFacilities, SkilledNursingFacilities, \
    HospiceFacilities, State, ZipCode


# Create your views here.
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


class HospiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HospiceFacilities.objects.all()
    serializer_class = HospiceFacilitiesSerializer


class StateListView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class ZipCodeListView(generics.ListCreateAPIView):
    queryset = ZipCode.objects.all()
    serializer_class = ZipCodeSerializer


class ZipCodeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ZipCode.objects.all()
    serializer_class = ZipCodeSerializer



