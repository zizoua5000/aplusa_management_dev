from django.urls import path
from device.api.views import DeviceListCreateAPIView,DeviceUpdateDeleteAPIView

app_name='device'
urlpatterns = [
    path('list_create/', DeviceListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', DeviceUpdateDeleteAPIView.as_view(),name='update_delete')
]
