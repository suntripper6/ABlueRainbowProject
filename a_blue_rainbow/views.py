from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView, View
from rest_framework import generics, permissions

from .forms import (
    AdminAuthenticationForm,
    AssistedLivingFacilityForm,
    HomeHealthFacilityForm,
    HospiceFacilityForm,
    SkilledNursingFacilityForm,
    UserFeedbackForm,
)
from .models import (
    AssistedLivingFacility,
    HomeHealthFacility,
    HospiceFacility,
    Provider,
    SkilledNursingFacility,
    State,
    UserFeedback,
)
from .serializer import (
    AssistedLivingFacilitySerializer,
    HomeHealthFacilitySerializer,
    HospiceFacilitySerializer,
    ProviderSerializer,
    SkilledNursingFacilitySerializer,
    StateSerializer,
    UserFeedbackSerializer,
)


def _first_named_match(queryset, query):
    cleaned_query = (query or "").strip()
    if not cleaned_query:
        return None
    return queryset.filter(name__icontains=cleaned_query).order_by("name").first()


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = "/login/"

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        raise PermissionDenied("Admin access is required.")


class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or bool(
            request.user and request.user.is_staff
        )


class AdminLoginPageView(LoginView):
    authentication_form = AdminAuthenticationForm
    template_name = "registration/login.html"
    redirect_authenticated_user = True


class HomePageView(TemplateView):
    template_name = "home-view.html"


class FacilityDirectorySearchView(TemplateView):
    template_name = "search_facilities.html"
    model = AssistedLivingFacility

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        searched = self.request.POST.get("searched", "") if self.request.method == "POST" else ""
        context.update(
            {
                "searched": searched,
                "object": _first_named_match(self.model.objects.all(), searched),
            }
        )
        return context

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class FacilityListPageView(ListView):
    paginate_by = 2
    ordering = ("name",)

    def get_queryset(self):
        return self.model.objects.order_by(*self.ordering)


class FacilityDetailPageView(DetailView):
    pk_url_kwarg = "id"


class FacilityCreatePageView(StaffRequiredMixin, CreateView):
    success_path = "create?submitted=True"

    def get_success_url(self):
        return self.success_path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submitted"] = "submitted" in self.request.GET
        return context


class FacilityUpdatePageView(StaffRequiredMixin, UpdateView):
    pk_url_kwarg = "id"
    success_path = "/"

    def get_success_url(self):
        return self.success_path


class FacilityDeletePageView(StaffRequiredMixin, View):
    model = None
    success_path = "/"

    def get(self, request, *args, **kwargs):
        return self._delete(kwargs["id"])

    def post(self, request, *args, **kwargs):
        return self._delete(kwargs["id"])

    def _delete(self, facility_id):
        get_object_or_404(self.model, pk=facility_id).delete()
        return HttpResponseRedirect(self.success_path)


class FacilitySearchPageView(TemplateView):
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = _first_named_match(self.model.objects.all(), self.request.GET.get("q", ""))
        return context


class AssistedLivingListPageView(FacilityListPageView):
    model = AssistedLivingFacility
    context_object_name = "alfs"
    template_name = "assistedliving/list.html"


class AssistedLivingDetailPageView(FacilityDetailPageView):
    model = AssistedLivingFacility
    context_object_name = "alf_obj"
    template_name = "assistedliving/detail.html"


class AssistedLivingCreatePageView(FacilityCreatePageView):
    form_class = AssistedLivingFacilityForm
    template_name = "assistedliving/create.html"


class AssistedLivingUpdatePageView(FacilityUpdatePageView):
    model = AssistedLivingFacility
    form_class = AssistedLivingFacilityForm
    context_object_name = "alf_obj"
    template_name = "assistedliving/update.html"
    success_path = "/assistedliving/list"


class AssistedLivingDeletePageView(FacilityDeletePageView):
    model = AssistedLivingFacility
    success_path = "/assistedliving/list"


class AssistedLivingSearchPageView(FacilitySearchPageView):
    model = AssistedLivingFacility
    template_name = "assistedliving/search.html"


class HomeHealthListPageView(FacilityListPageView):
    model = HomeHealthFacility
    context_object_name = "hhcs"
    template_name = "homehealth/list.html"


class HomeHealthDetailPageView(FacilityDetailPageView):
    model = HomeHealthFacility
    context_object_name = "hhc_obj"
    template_name = "homehealth/detail.html"


class HomeHealthCreatePageView(FacilityCreatePageView):
    form_class = HomeHealthFacilityForm
    template_name = "homehealth/create.html"


class HomeHealthUpdatePageView(FacilityUpdatePageView):
    model = HomeHealthFacility
    form_class = HomeHealthFacilityForm
    context_object_name = "hhc_obj"
    template_name = "homehealth/update.html"
    success_path = "/homehealth/list"


class HomeHealthDeletePageView(FacilityDeletePageView):
    model = HomeHealthFacility
    success_path = "/homehealth/list"


class HomeHealthSearchPageView(FacilitySearchPageView):
    model = HomeHealthFacility
    template_name = "homehealth/search.html"


class SkilledNursingListPageView(FacilityListPageView):
    model = SkilledNursingFacility
    context_object_name = "snfs"
    template_name = "skillednursing/list.html"


class SkilledNursingDetailPageView(FacilityDetailPageView):
    model = SkilledNursingFacility
    context_object_name = "snf_obj"
    template_name = "skillednursing/detail.html"


class SkilledNursingCreatePageView(FacilityCreatePageView):
    form_class = SkilledNursingFacilityForm
    template_name = "skillednursing/create.html"


class SkilledNursingUpdatePageView(FacilityUpdatePageView):
    model = SkilledNursingFacility
    form_class = SkilledNursingFacilityForm
    context_object_name = "snf_obj"
    template_name = "skillednursing/update.html"
    success_path = "/skillednursing/list"


class SkilledNursingDeletePageView(FacilityDeletePageView):
    model = SkilledNursingFacility
    success_path = "/skillednursing/list"


class SkilledNursingSearchPageView(FacilitySearchPageView):
    model = SkilledNursingFacility
    template_name = "skillednursing/search.html"


class HospiceListPageView(FacilityListPageView):
    model = HospiceFacility
    context_object_name = "hosps"
    template_name = "hospice/list.html"


class HospiceDetailPageView(FacilityDetailPageView):
    model = HospiceFacility
    context_object_name = "hospice_obj"
    template_name = "hospice/detail.html"


class HospiceCreatePageView(FacilityCreatePageView):
    form_class = HospiceFacilityForm
    template_name = "hospice/create.html"


class HospiceUpdatePageView(FacilityUpdatePageView):
    model = HospiceFacility
    form_class = HospiceFacilityForm
    context_object_name = "hospice_obj"
    template_name = "hospice/update.html"
    success_path = "/hospice/list"


class HospiceDeletePageView(FacilityDeletePageView):
    model = HospiceFacility
    success_path = "/hospice/list"


class HospiceSearchPageView(FacilitySearchPageView):
    model = HospiceFacility
    template_name = "hospice/search.html"


home_view = HomePageView.as_view()
search_facilities = FacilityDirectorySearchView.as_view()

alf_list_view = AssistedLivingListPageView.as_view()
alf_detail_view = AssistedLivingDetailPageView.as_view()
alf_create_view = AssistedLivingCreatePageView.as_view()
alf_update_view = AssistedLivingUpdatePageView.as_view()
alf_delete_view = AssistedLivingDeletePageView.as_view()
alf_search_view = AssistedLivingSearchPageView.as_view()

hhc_list_view = HomeHealthListPageView.as_view()
hhc_detail_view = HomeHealthDetailPageView.as_view()
hhc_create_view = HomeHealthCreatePageView.as_view()
hhc_update_view = HomeHealthUpdatePageView.as_view()
hhc_delete_view = HomeHealthDeletePageView.as_view()
hhc_search_view = HomeHealthSearchPageView.as_view()

snf_list_view = SkilledNursingListPageView.as_view()
snf_detail_view = SkilledNursingDetailPageView.as_view()
snf_create_view = SkilledNursingCreatePageView.as_view()
snf_update_view = SkilledNursingUpdatePageView.as_view()
snf_delete_view = SkilledNursingDeletePageView.as_view()
snf_search_view = SkilledNursingSearchPageView.as_view()

hospice_list_view = HospiceListPageView.as_view()
hospice_detail_view = HospiceDetailPageView.as_view()
hospice_create_view = HospiceCreatePageView.as_view()
hospice_update_view = HospiceUpdatePageView.as_view()
hospice_delete_view = HospiceDeletePageView.as_view()
hospice_search_view = HospiceSearchPageView.as_view()


class UserFeedbackCreatePageView(CreateView):
    form_class = UserFeedbackForm
    template_name = "userfeedback/feedback.html"
    success_url = "/?submitted"


userfeedback_create_view = UserFeedbackCreatePageView.as_view()


class OrderedListCreateAPIView(generics.ListCreateAPIView):
    ordering = ()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by(*self.ordering) if self.ordering else queryset


class OrderedFacilityListView(OrderedListCreateAPIView):
    ordering = ("name",)
    permission_classes = [IsStaffOrReadOnly]


class FacilityDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsStaffOrReadOnly]


class UserFeedbackListView(generics.ListCreateAPIView):
    queryset = UserFeedback.objects.order_by("name", "id")
    serializer_class = UserFeedbackSerializer


class UserFeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserFeedback.objects.all()
    serializer_class = UserFeedbackSerializer


class HomeHealthListView(OrderedFacilityListView):
    queryset = HomeHealthFacility.objects.all()
    serializer_class = HomeHealthFacilitySerializer


class HomeHealthDetailView(FacilityDetailApiView):
    queryset = HomeHealthFacility.objects.all()
    serializer_class = HomeHealthFacilitySerializer


class AssistedLivingListView(OrderedFacilityListView):
    queryset = AssistedLivingFacility.objects.all()
    serializer_class = AssistedLivingFacilitySerializer


class AssistedLivingDetailView(FacilityDetailApiView):
    queryset = AssistedLivingFacility.objects.all()
    serializer_class = AssistedLivingFacilitySerializer


class SkilledNursingListView(OrderedFacilityListView):
    queryset = SkilledNursingFacility.objects.all()
    serializer_class = SkilledNursingFacilitySerializer


class SkilledNursingDetailView(FacilityDetailApiView):
    queryset = SkilledNursingFacility.objects.all()
    serializer_class = SkilledNursingFacilitySerializer


class HospiceListView(OrderedFacilityListView):
    queryset = HospiceFacility.objects.all()
    serializer_class = HospiceFacilitySerializer


class HospiceDetailView(FacilityDetailApiView):
    queryset = HospiceFacility.objects.all()
    serializer_class = HospiceFacilitySerializer


class StateListView(OrderedListCreateAPIView):
    queryset = State.objects.all()
    ordering = ("state", "city", "zip_code")
    serializer_class = StateSerializer


class StateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class ProviderListView(OrderedListCreateAPIView):
    queryset = Provider.objects.all()
    ordering = ("facility_type", "facility_name")
    serializer_class = ProviderSerializer


class ProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer