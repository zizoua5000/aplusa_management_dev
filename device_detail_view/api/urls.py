from django.urls import path
from device_detail_view.api.views import DeviceDetailViewListCreateAPIView,DeviceDetailViewListCreateAPIView

app_name='device_detail_view'
urlpatterns = [
    path('list_create/', DeviceDetailViewListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', DeviceDetailViewListCreateAPIView.as_view(),name='update_delete')
]
