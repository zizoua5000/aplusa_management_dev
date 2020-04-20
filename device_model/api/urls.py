from django.urls import path
from device_model.api.views import DeviceModelListCreateAPIView,DeviceModelUpdateDeleteAPIView

app_name='device_model'
urlpatterns = [
    path('list_create/', DeviceModelListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', DeviceModelUpdateDeleteAPIView.as_view(),name='update_delete')
]
