from django.shortcuts import render

from .models import ItemLibrary
from django.http import HttpResponse


# Create your views here.


def form_page(request, *args, **kwargs):
    return render(request, 'itemform.html')


def register(request, *args, **kwargs):
    return render(request, 'register.html')


def item_view(request, *args, **kwargs):
    item_libraty = ItemLibrary.objects.all()

    context = {
        'object': item_libraty
    }
    return render(request, 'datatable.html')


def cat_view(request, *args, **kwargs):
    return render(request, 'category.html')
