from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View

from .forms import ContactForm, PhoneNumberFormSet
from .models import Contact
from .utils import get_objects_with_paginator


class ContactListView(ListView):
    template_name = "contacts/contact_list.html"

    def get_queryset(self):
        return get_objects_with_paginator(
            items=Contact.objects.all(), request=self.request, objects_count=30
        )


class ContactDetailView(DetailView):
    template_name = "contacts/contact_detail.html"
    context_object_name = "contact"

    def get_queryset(self):
        return Contact.objects.filter(id=self.kwargs["pk"])


class AddContactView(View):
    def get(self, *args, **kwargs):
        contact_form = ContactForm()
        phone_number_formset = PhoneNumberFormSet()
        return render(
            self.request,
            "contacts/add_contact.html",
            {
                "contact_form": contact_form,
                "phone_number_formset": phone_number_formset,
            },
        )

    def post(self, *args, **kwargs):
        contact_form = ContactForm(self.request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            phone_number_formset = PhoneNumberFormSet(
                self.request.POST, instance=contact
            )
            if phone_number_formset.is_valid():
                phone_number_formset.save()
                return redirect("contact-list")
        else:
            phone_number_formset = PhoneNumberFormSet(self.request.POST)
        return render(
            self.request,
            "contacts/add_contact.html",
            {
                "contact_form": contact_form,
                "phone_number_formset": phone_number_formset,
            },
        )
