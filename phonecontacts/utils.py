from django.core.paginator import Paginator


def get_objects_with_paginator(items, request, objects_count):
    paginator = Paginator(items, objects_count)
    page = request.GET.get("p", None)
    items = paginator.get_page(page)
    return items
