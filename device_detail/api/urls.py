from django.urls import path
from device_detail.api.views import DeviceDetailListCreateAPIView,DeviceDetailUpdateDeleteAPIView

app_name='device_detail'
urlpatterns = [
    path('list_create/', DeviceDetailListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', DeviceDetailUpdateDeleteAPIView.as_view(),name='update_delete')
]
