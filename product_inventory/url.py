from django.urls import path
from product_inventory.views import form_page, item_view, cat_view

urlpatterns = [

    path('form/', form_page),
    path('datatable.html', item_view),
    path('category.html', cat_view)

]
