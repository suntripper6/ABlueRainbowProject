from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import ModelForm
from .models import HospiceFacility, AssistedLivingFacility, HomeHealthFacility, SkilledNursingFacility, UserFeedback


class BaseFacilityForm(ModelForm):
    class Meta:
        fields = ("name", "address", "city", "state", "zip_code")
        labels = {
            "name": "",
            "address": "",
            "city": "",
            "state": "",
            "zip_code": "",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Facility Name"}),
            "address": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Facility Address"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Facility City"}),
            "state": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Facility State"}),
            "zip_code": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Facility Zip Code"}),
        }


class HospiceFacilityForm(BaseFacilityForm):
    class Meta:
        model = HospiceFacility
        fields = BaseFacilityForm.Meta.fields
        labels = BaseFacilityForm.Meta.labels
        widgets = BaseFacilityForm.Meta.widgets


class AssistedLivingFacilityForm(BaseFacilityForm):
    class Meta:
        model = AssistedLivingFacility
        fields = BaseFacilityForm.Meta.fields
        labels = BaseFacilityForm.Meta.labels
        widgets = BaseFacilityForm.Meta.widgets


class HomeHealthFacilityForm(BaseFacilityForm):
    class Meta:
        model = HomeHealthFacility
        fields = BaseFacilityForm.Meta.fields
        labels = BaseFacilityForm.Meta.labels
        widgets = BaseFacilityForm.Meta.widgets


class SkilledNursingFacilityForm(BaseFacilityForm):
    class Meta:
        model = SkilledNursingFacility
        fields = BaseFacilityForm.Meta.fields
        labels = BaseFacilityForm.Meta.labels
        widgets = BaseFacilityForm.Meta.widgets


class UserFeedbackForm(ModelForm):
    class Meta:
        model = UserFeedback
        fields = ("name", "email", "comments")
        labels = {
            "name": "",
            "email": "",
            "comments": "",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email address"}),
            "comments": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter your comments"}),
        }


class AdminAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Admin username", "autofocus": True}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Password"}
        )
