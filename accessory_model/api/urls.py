from django.urls import path
from accessory_model.api.views import AccessoryModelListCreateAPIView,AccessoryModelUpdateDeleteAPIView

app_name='accessory_model'
urlpatterns = [
    path('list_create/', AccessoryModelListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', AccessoryModelUpdateDeleteAPIView.as_view(),name='update_delete')
]
