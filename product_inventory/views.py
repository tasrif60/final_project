from django.shortcuts import render, redirect
from .form import CategoryForm, ItemlistForm

from .models import ItemLibrary, Category, Itemlist
from django.http import HttpResponse


# Create your views here.
def form_page(request, *args, **kwargs):
    return render(request, 'itemform.html')

def register(request, *args, **kwargs):
    return render(request, 'register.html')





def view_item(request, *args, **kwargs):
    item_libraty = ItemLibrary.objects.all()

    context = {
        'object': item_libraty
    }
    return render(request, 'datatable.html', context)



def view_category(request, *args, **kwargs):
    item_libraty = Category.objects.all()

    context = {
        'object': item_libraty
    }
    return render(request, 'category.html', context)


def create_category(request, *args, **kwargs):

    if request.method == 'POST':
        prof_form = CategoryForm(request.POST)
        if prof_form.is_valid():
            prof_form.save(commit=True)
            return redirect('category.html')

    form = CategoryForm()
    return render(request, 'categoryform.html', {'form': form})



def create_itemlist(request, *args, **kwargs):

    if request.method == 'POST':
        prof_form = Itemlist(request.POST)
        if prof_form.is_valid():
            prof_form.save(commit=True)
            return redirect('datatable.html')

    form = ItemlistForm()
    return render(request, 'itemlistform.html', {'form': form})

