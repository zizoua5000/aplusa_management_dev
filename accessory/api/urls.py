from django.urls import path
from accessory.api.views import AccessoryListCreateAPIView,AccessoryUpdateDeleteAPIView

app_name='accessory'
urlpatterns = [
    path('list_create/', AccessoryListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', AccessoryUpdateDeleteAPIView.as_view(),name='update_delete')
]
