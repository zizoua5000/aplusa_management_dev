from django.urls import path
from vehicle_type.api.views import VehicleTypeListCreateAPIView,VehicleTypeUpdateDeleteAPIView

app_name='vehicle_type'
urlpatterns = [
    path('list_create/', VehicleTypeListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', VehicleTypeUpdateDeleteAPIView.as_view(),name='update_delete')
]
