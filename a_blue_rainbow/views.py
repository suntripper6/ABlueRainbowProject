from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
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

class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or bool(
            request.user and request.user.is_staff
        )

class OrderedListCreateAPIView(generics.ListCreateAPIView):
    ordering = ()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by(*self.ordering) if self.ordering else queryset

class OrderedFacilityListView(OrderedListCreateAPIView):
    ordering = ("name",)
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["city", "state", "zip_code"]
    search_fields = ["name", "address", "city", "state", "zip_code"]

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
