from django import forms
from .models import Prediction


class PredictForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=[('Fresh Vegitable', 'Fresh Vegitable'), ('Grocery', 'Grocery'), ('Fish', 'Fish'), ('Beef', 'Beef'),
                 ('Ready Made Food', 'Ready Made Food'), ('Frozen', 'Frozen'), ('Spices', 'Spices'), ('Goat', 'Goat'),
                 ('Chicken', 'Chicken'), ('Sweet', 'Sweet'), ('Beef Share', 'Beef Share'), ('Cosmetic', 'Cosmetic'),
                 ('Achar', 'Achar'), ('Beverages', 'Beverages'), ('Lamb', 'Lamb')])

    category.widget.attrs.update({'class': 'custom-select'})

    product = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gross_sale = forms.FloatField(max_value=50, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    qty = forms.FloatField(max_value=50, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    month = forms.IntegerField(max_value=50, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Prediction
        fields = "__all__"
