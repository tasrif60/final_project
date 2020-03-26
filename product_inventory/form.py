from django import forms
from .models import Category
from .models import Itemlist


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"



class ItemlistForm(forms.ModelForm):
    class Meta:
        model = Itemlist
        fields = "__all__"