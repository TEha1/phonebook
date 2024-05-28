from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("name"),
        help_text=_("the name of the contact"),
    )

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    contact = models.ForeignKey(
        Contact,
        related_name="phone_numbers",
        on_delete=models.CASCADE,
        verbose_name=_("contact"),
        help_text=_("the contact of the phone"),
    )
    number = PhoneNumberField(blank=False, null=False)

    def __str__(self):
        return f"{self.number} - {self.contact.name}"
