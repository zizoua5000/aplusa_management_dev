from django.urls import path
from price.api.views import PriceListCreateAPIView,PriceUpdateDeleteAPIView

app_name='price'
urlpatterns = [
    path('list_create/', PriceListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', PriceUpdateDeleteAPIView.as_view(),name='update_delete')
]
