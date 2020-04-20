from django.urls import path
from device_mark.api.views import DeviceMarkListCreateAPIView,DeviceMarkUpdateDeleteAPIView

app_name='device_mark'
urlpatterns = [
    path('list_create/', DeviceMarkListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', DeviceMarkUpdateDeleteAPIView.as_view(),name='update_delete')
]
