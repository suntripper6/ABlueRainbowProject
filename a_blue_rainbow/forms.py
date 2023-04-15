from django import forms
from django.forms import ModelForm
from .models import HospiceFacilities, AssistedLivingFacilities, HomeHealthFacilities, SkilledNursingFacilities, UserFeedback


class HospiceForm(ModelForm):
    class Meta:
        model = HospiceFacilities
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


class AssistedLivingForm(ModelForm):
    class Meta:
        model = AssistedLivingFacilities
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


class HomeHealthForm(ModelForm):
    class Meta:
        model = HomeHealthFacilities
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


class SkilledNursingForm(ModelForm):
    class Meta:
        model = SkilledNursingFacilities
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


class FeedbackForm(ModelForm):
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
