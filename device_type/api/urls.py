from django.urls import path
from device_type.api.views import DeviceTypeListCreateAPIView,DeviceTypeUpdateDeleteAPIView

app_name='device_type'
urlpatterns = [
    path('list_create/', DeviceTypeListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', DeviceTypeUpdateDeleteAPIView.as_view(),name='update_delete')
]
