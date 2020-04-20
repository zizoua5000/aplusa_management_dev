from django.urls import path
from region.api.views import RegionListCreateAPIView,RegionUpdateDeleteAPIView

app_name='region'
urlpatterns = [
    path('list_create/', RegionListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', RegionUpdateDeleteAPIView.as_view(),name='update_delete')
]
