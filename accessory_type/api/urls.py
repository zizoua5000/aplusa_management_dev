from django.urls import path
from accessory_type.api.views import AccessoryTypeListCreateAPIView,AccessoryTypeUpdateDeleteAPIView

app_name='accessory_type'
urlpatterns = [
    path('list_create/', AccessoryTypeListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', AccessoryTypeUpdateDeleteAPIView.as_view(),name='update_delete')
]
