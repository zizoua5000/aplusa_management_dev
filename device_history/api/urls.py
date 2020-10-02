from django.urls import path
from device_history.api.views import DeviceHistoryListCreateAPIView,DeviceHistoryUpdateDeleteAPIView

app_name='device_history'
urlpatterns = [
    path('list_create/', DeviceHistoryListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', DeviceHistoryUpdateDeleteAPIView.as_view(),name='update_delete')
]
