from django.urls import path
from vehicle_mark.api.views import VehicleMarkListCreateAPIView,VehicleMarkUpdateDeleteAPIView

app_name='vehicle_mark'
urlpatterns = [
    path('list_create/', VehicleMarkListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', VehicleMarkUpdateDeleteAPIView.as_view(),name='update_delete')
]
