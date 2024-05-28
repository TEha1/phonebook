from django.urls import path
from .views import ContactListView, ContactDetailView, AddContactView

urlpatterns = [
    path("", ContactListView.as_view(), name="contact-list"),
    path("contact/<int:pk>/", ContactDetailView.as_view(), name="contact-detail"),
    path("add/", AddContactView.as_view(), name="add-contact"),
]
