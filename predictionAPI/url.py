from django.urls import path, include
from predictionAPI.views import predict_svm, PredictionView, form_view, sold_product
from rest_framework import routers

router = routers.DefaultRouter()
router.register('predictionAPI', PredictionView)
urlpatterns = [
    # path('form/', views.myform, name='myform'),
    path('api/', include(router.urls)),
    path('status/', predict_svm),
    path('form.html', form_view),
    path('sold.html', sold_product)

]
