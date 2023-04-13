from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from rest_framework import generics
from rest_framework.views import APIView
from .serializer import UserFeedBackSerializer, HomeHealthFacilitiesSerializer, AssistedLivingFacilitiesSerializer, \
    SkilledNursingFacilitiesSerializer, HospiceFacilitiesSerializer, StateSerializer, ProviderSerializer
from .models import UserFeedback, HomeHealthFacilities, AssistedLivingFacilities, SkilledNursingFacilities, \
    HospiceFacilities, States, Providers
from .forms import HospiceForm


# PROVIDER SELECTION


def home_view(request):
    provider_qs = Providers.objects.all()
    assisted_qs = AssistedLivingFacilities.objects.all()
    homehealth_qs = HomeHealthFacilities.objects.all()
    skillednursing_qs = SkilledNursingFacilities.objects.all()
    hospice_qs = HospiceFacilities.objects.all()
    states_qs = States.objects.order_by("state").values_list(
        "state", flat=True).distinct("state")

    context = {
        "provider_qs": provider_qs,
        "assisted_qs": assisted_qs,
        "homehealth_qs": homehealth_qs,
        "skillednursing_qs": skillednursing_qs,
        "hospice_qs": hospice_qs,
        "states_qs": states_qs,
    }

    return render(request, "home-view.html", context=context)


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

# def hospice_create_view(request, id=None):
#     submitted = False

#     if request.method == "POST":
#         form = HospiceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/?submitted=True")
#     else:
#         form = HospiceForm
#         if "submitted" in request.Get:
#             submitted = True

#     context = {
#         "form": form,
#         "submitted": submitted
#     }

#     return render(request, "hospice/update.html", context=context)


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

    print(hospice_obj)

    context = {
        "object": hospice_obj,
    }

    return render(request, "hospice/search.html", context=context)


def hospice_create_view(request):
    context = {}

    if request.method == "POST":
        name = request.POST.get("name")
        print(name)
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zipcode = request.POST.get("zip_code")
        hospice = HospiceFacilities.objects.create(
            name=name, address=address, city=city, state=state, zip_code=zipcode, facility_type_id=3,
            phone_number="", medicare_elig="", map="", rating=0, reviews="", official_website="")

        hospice.save()
        context["created"] = True

    return render(request, "hospice/create.html", context=context)


def userfeedback_create_view(request):
    context = {}

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        comments = request.POST.get("comments")
        UserFeedback.objects.create(
            name=name, email=email, comments=comments)
        context["created"] = True

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
