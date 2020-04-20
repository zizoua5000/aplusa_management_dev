from django.urls import path
from device_location.api.views import DeviceLocationListCreateAPIView,DeviceLocationUpdateDeleteAPIView

app_name='device_location'
urlpatterns = [
    path('list_create/', DeviceLocationListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', DeviceLocationUpdateDeleteAPIView.as_view(),name='update_delete')
]
