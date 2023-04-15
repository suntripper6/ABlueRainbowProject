from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from rest_framework import generics
from rest_framework.views import APIView
from .serializer import UserFeedBackSerializer, HomeHealthFacilitiesSerializer, AssistedLivingFacilitiesSerializer, \
    SkilledNursingFacilitiesSerializer, HospiceFacilitiesSerializer, StateSerializer, ProviderSerializer
from .models import UserFeedback, HomeHealthFacilities, AssistedLivingFacilities, SkilledNursingFacilities, \
    HospiceFacilities, States, Providers
from .forms import HospiceForm, HomeHealthForm, AssistedLivingForm, SkilledNursingForm, FeedbackForm
from django.core.paginator import Paginator


# HOME VIEW
def home_view(request):
    provider_qs = Providers.objects.all()
    assisted_qs = AssistedLivingFacilities.objects.all()
    homehealth_qs = HomeHealthFacilities.objects.all()
    skillednursing_qs = SkilledNursingFacilities.objects.all()
    hospice_qs = HospiceFacilities.objects.all()
    states_qs = States.objects.order_by("state").values_list(
        "state", flat=True).distinct("state")

    snf_p = Paginator(SkilledNursingFacilities.objects.all(), 2)
    page = request.GET.get("page")
    snfs = snf_p.get_page(page)

    context = {
        "provider_qs": provider_qs,
        "assisted_qs": assisted_qs,
        "homehealth_qs": homehealth_qs,
        "skillednursing_qs": skillednursing_qs,
        "snfs": snfs,
        "hospice_qs": hospice_qs,
        "states_qs": states_qs,
    }

    return render(request, "home-view.html", context=context)


def hospice_list_view(request):
    hospice_qs = HospiceFacilities.objects.all()
    context = {
        "hospice_qs": hospice_qs
    }

    return render(request, "hospice/list.html", context=context)


# SELECT FACILITY


# SEARCH FACILITIES
def search_facilities(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        alf = AssistedLivingFacilities.objects.filter(
            name__icontains=searched).get()
        return render(request, "search_facilities.html", {"searched": searched, "object": alf})


# ASSISTED LIVING VIEWS
def alf_view(request):
    alf_qs = AssistedLivingFacilities.objects.get()

    context = {
        "alf_qs": alf_qs
    }

    return render(request, "assistedliving-view.html", context=context)


def alf_detail_view(request, id=None):
    alf_obj = None

    if id is not None:
        alf_obj = AssistedLivingFacilities.objects.get(id=id)

    context = {
        "alf_obj": alf_obj
    }

    return render(request, "assistedliving/detail.html", context=context)


def alf_update_view(request, id):
    alf_obj = AssistedLivingFacilities.objects.get(id=id)
    form = AssistedLivingForm(request.POST or None, instance=alf_obj)

    context = {
        "alf_obj": alf_obj,
        "form": form
    }

    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, "assistedliving/update.html", context=context)


def alf_delete_view(request, id=None):
    alf_obj = None

    if id is not None:
        alf_obj = AssistedLivingFacilities.objects.get(pk=id)
        alf_obj.delete()

    return redirect("/")


def alf_search_view(request):
    query_dict = request.GET
    query = query_dict.get("q")
    alf_obj = None

    try:
        query = query_dict.get("q")
    except:
        query = None

    if query is not None:
        alf_obj = AssistedLivingFacilities.objects.filter(
            name__icontains=query).get()

    context = {
        "object": alf_obj,
    }

    return render(request, "assistedliving/search.html", context=context)


# HOMEHEALTHCARE VIEWS
def hhc_view(request):
    hhc_qs = HomeHealthFacilities.objects.get()

    context = {
        "hhc_qs": hhc_qs
    }

    return render(request, "homehealth-view.html", context=context)


def hhc_detail_view(request, id=None):
    hhc_obj = None

    if id is not None:
        hhc_obj = HomeHealthFacilities.objects.get(id=id)

    context = {
        "hhc_obj": hhc_obj
    }

    return render(request, "homehealth/detail.html", context=context)


def hhc_update_view(request, id):
    hhc_obj = HomeHealthFacilities.objects.get(id=id)
    form = HomeHealthForm(request.POST or None, instance=hhc_obj)

    context = {
        "hhc_obj": hhc_obj,
        "form": form
    }

    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, "homehealth/update.html", context=context)


def hhc_delete_view(request, id=None):
    hhc_obj = None

    if id is not None:
        hhc_obj = HomeHealthFacilities.objects.get(pk=id)
        hhc_obj.delete()

    return redirect("/")


def hhc_search_view(request):
    query_dict = request.GET
    query = query_dict.get("q")
    hhc_obj = None

    try:
        query = query_dict.get("q")
    except:
        query = None

    if query is not None:
        hhc_obj = HomeHealthFacilities.objects.filter(
            name__icontains=query).get()

    context = {
        "object": hhc_obj,
    }

    return render(request, "homehealth/search.html", context=context)


# SKILLED NURSING VIEWS
def snf_view(request):
    snf_qs = SkilledNursingFacilities.objects.get()

    context = {
        "snf_qs": snf_qs
    }

    return render(request, "skillednursing-view.html", context=context)


def snf_detail_view(request, id=None):
    snf_obj = None

    if id is not None:
        snf_obj = SkilledNursingFacilities.objects.get(id=id)

    context = {
        "snf_obj": snf_obj
    }

    return render(request, "skillednursing/detail.html", context=context)


def snf_update_view(request, id):
    snf_obj = SkilledNursingFacilities.objects.get(id=id)
    form = SkilledNursingForm(request.POST or None, instance=snf_obj)

    context = {
        "snf_obj": snf_obj,
        "form": form
    }

    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, "skillednursing/update.html", context=context)


def snf_delete_view(request, id=None):
    snf_obj = None

    if id is not None:
        snf_obj = SkilledNursingFacilities.objects.get(pk=id)
        snf_obj.delete()

    return redirect("/")


def snf_search_view(request):
    query_dict = request.GET
    query = query_dict.get("q")
    snf_obj = None

    try:
        query = query_dict.get("q")
    except:
        query = None

    if query is not None:
        snf_obj = HomeHealthFacilities.objects.filter(
            name__icontains=query).get()

    context = {
        "object": snf_obj,
    }

    return render(request, "skillednursing/search.html", context=context)


# HOSPICE VIEWS
def hospice_view(request):
    hospice_qs = HospiceFacilities.objects.all()

    context = {
        "hospice_qs": hospice_qs
    }

    return render(request, "hospice-view.html", context=context)


def hospice_detail_view(request, id=None):
    hospice_obj = None

    if id is not None:
        hospice_obj = HospiceFacilities.objects.get(id=id)

    context = {
        "hospice_obj": hospice_obj
    }

    return render(request, "hospice/detail.html", context=context)


def hospice_update_view(request, id):
    hospice_obj = HospiceFacilities.objects.get(id=id)
    form = HospiceForm(request.POST or None, instance=hospice_obj)

    context = {
        "hospice_obj": hospice_obj,
        "form": form
    }

    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, "hospice/update.html", context=context)


def hospice_delete_view(request, id=None):
    hospice_obj = None

    if id is not None:
        hospice_obj = HospiceFacilities.objects.get(pk=id)
        hospice_obj.delete()

    return redirect("/")


def hospice_search_view(request):
    query_dict = request.GET
    query = query_dict.get("q")
    hospice_obj = None

    try:
        query = query_dict.get("q")
    except:
        query = None

    if query is not None:
        hospice_obj = HospiceFacilities.objects.filter(
            name__icontains=query).get()

    context = {
        "object": hospice_obj,
    }

    return render(request, "hospice/search.html", context=context)


def hospice_create_view(request):
    form = HospiceForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/?submitted")

    context = {
        "form": form,
    }

    return render(request, "userfeedback/feedback.html", context=context)
    # context = {}

    # if request.method == "POST":
    #     name = request.POST.get("name")
    #     address = request.POST.get("address")
    #     city = request.POST.get("city")
    #     state = request.POST.get("state")
    #     zipcode = request.POST.get("zip_code")
    #     hospice = HospiceFacilities.objects.create(
    #         name=name, address=address, city=city, state=state, zip_code=zipcode, facility_type_id=3,
    #         phone_number="", medicare_elig="", map="", rating=0, reviews="", official_website="")

    #     hospice.save()
    #     context["created"] = True

    # return render(request, "hospice/create.html", context=context)


# USER FEEDBACK
def userfeedback_create_view(request):
    form = FeedbackForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/?submitted")

    context = {
        "form": form,
    }

    return render(request, "userfeedback/feedback.html", context=context)


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
