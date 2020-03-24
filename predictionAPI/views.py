from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Prediction
from .serializers import PredictionSerializers
import joblib
import pandas as pd
from .form import PredictForm
from django.contrib import messages
from django.db.models import Sum


# Create your views here.

class PredictionView(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializers


def text_value(df):
    ohe_col = joblib.load("/Users/tasrifahmed/PyProjects/final_project//allcollumn.pkl")
    print(ohe_col)
    cat_columns = ['category']
    df_processed = pd.get_dummies(df, columns=cat_columns)
    print(df_processed)
    # df_list = df_processed.columns.to_numpy()
    newdict = {}
    for i in ohe_col:
        if i in df_processed:
            newdict[i] = df_processed[i].values
        else:
            newdict[i] = 0
    newdf = pd.DataFrame(newdict)
    return newdf


# @api_view(["POST"])
def predict_svm(unit):
    try:
        mdl = joblib.load("/Users/tasrifahmed/PyProjects/final_project/product_model.pkl")
        y_pred = mdl.predict(unit)
        print(y_pred)
        newdf = pd.DataFrame(y_pred, columns=['class'])
        newdf = newdf.replace({1: 'Low', 2: 'Medium', 3: 'High'})
        return format(newdf.values)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def form_view(request):
    if request.method == 'POST':
        form = PredictForm(request.POST)
        if form.is_valid():
            Category = form.cleaned_data['category']
            Product = form.cleaned_data['product']
            Gross_sale = form.cleaned_data['gross_sale']
            Qty = form.cleaned_data['qty']
            Month = form.cleaned_data['month']
            myDictionary = request.POST.dict()
            print(myDictionary)
            DataFM = pd.DataFrame(myDictionary, index=[0])
            answer = text_value(DataFM)
            final_answer = predict_svm(answer)
            messages.success(request, 'Inventory Status: {}'.format(final_answer))
            form.save(commit=True)

    form = PredictForm()

    return render(request, 'form.html', {'form': form})


def sold_product(request, *args, **kwargs):
    sold_items = Prediction.objects.all()
    qty_only = list(Prediction.objects.aggregate(sum_qty=Sum('qty')).values())[0]
    total_sale = list(Prediction.objects.aggregate(Sum('gross_sale')).values())[0]
    contex = {
        'object': sold_items,
        'total_qty': qty_only,
        'total_sale': total_sale

    }
    return render(request, 'sold.html', contex)
