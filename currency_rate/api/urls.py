from django.urls import path
from currency_rate.api.views import CurrencyRateListCreateAPIView,CurrencyRateUpdateDeleteAPIView

app_name='currency_rate'
urlpatterns = [
    path('list_create/', CurrencyRateListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', CurrencyRateUpdateDeleteAPIView.as_view(),name='update_delete')
]
