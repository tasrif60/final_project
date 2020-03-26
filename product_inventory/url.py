from django.urls import path
from product_inventory.views import form_page, view_item, view_category, create_category, create_itemlist

urlpatterns = [

    path('form/', form_page),
    path('datatable.html', view_item),
    path('category.html', view_category),
    path('categoryform.html', create_category),
    path('itemlistform.html', create_itemlist)

]
