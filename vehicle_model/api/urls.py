from django.urls import path
from vehicle_model.api.views import VehicleModelListCreateAPIView,VehicleModelUpdateDeleteAPIView

app_name='vehicle_model'
urlpatterns = [
    path('list_create/', VehicleModelListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', VehicleModelUpdateDeleteAPIView.as_view(),name='update_delete')
]
