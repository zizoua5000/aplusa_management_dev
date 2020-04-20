from django.urls import path
from price_type.api.views import PriceTypeListCreateAPIView,PriceTypeUpdateDeleteAPIView

app_name='price_type'
urlpatterns = [
    path('list_create/', PriceTypeListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', PriceTypeUpdateDeleteAPIView.as_view(),name='update_delete')
]
