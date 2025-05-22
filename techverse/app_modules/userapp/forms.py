from django import forms
from . import models


class ContactEnquiryForm(forms.ModelForm):
    class Meta:
        model = models.ContactEnquiry
        fields = "__all__"