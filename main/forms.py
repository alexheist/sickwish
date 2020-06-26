from django import forms

from . import models


class InquiryForm(forms.ModelForm):
    class Meta:
        model = models.Inquiry
        fields = ("name", "email", "message")
