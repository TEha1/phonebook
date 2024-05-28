from django import forms
from phonenumber_field.formfields import PhoneNumberField as FormPhoneNumberField

from .models import Contact, PhoneNumber


class PhoneNumberForm(forms.ModelForm):
    number = FormPhoneNumberField(
        widget=forms.TextInput(attrs={"required": "required"})
    )

    class Meta:
        model = PhoneNumber
        fields = ["number"]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


PhoneNumberFormSet = forms.inlineformset_factory(
    Contact, PhoneNumber, form=PhoneNumberForm, extra=3
)
