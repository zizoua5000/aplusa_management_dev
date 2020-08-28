from django.urls import path
from m_vehicle_accessory.api.views import MVehicleAccessoryListCreateAPIView,MVehicleAccessoryUpdateDeleteAPIView

app_name='m_vehicle_accessory'
urlpatterns = [
    path('list_create/', MVehicleAccessoryListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', MVehicleAccessoryUpdateDeleteAPIView.as_view(),name='update_delete')
]
