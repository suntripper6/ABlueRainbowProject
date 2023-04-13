from django import forms
from django.forms import ModelForm
from .models import HospiceFacilities


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
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "state": forms.TextInput(attrs={"class": "form-control"}),
            "zip_code": forms.TextInput(attrs={"class": "form-control"}),
        }
