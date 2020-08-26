from django.urls import path
from accessory_fixing.api.views import AccessoryFixingListCreateAPIView,AccessoryFixingUpdateDeleteAPIView

app_name='accessory_fixing'
urlpatterns = [
    path('list_create/', AccessoryFixingListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', AccessoryFixingUpdateDeleteAPIView.as_view(),name='update_delete')
]
