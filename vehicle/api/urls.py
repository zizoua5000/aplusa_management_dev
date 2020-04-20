from django.urls import path
from vehicle.api.views import VehicleListCreateAPIView,VehicleUpdateDeleteAPIView

app_name='vehicle'
urlpatterns = [
    path('list_create/', VehicleListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', VehicleUpdateDeleteAPIView.as_view(),name='update_delete')
]
