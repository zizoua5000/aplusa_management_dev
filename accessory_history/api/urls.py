from django.urls import path
from accessory_history.api.views import AccessoryHistoryListCreateAPIView,AccessoryHistoryUpdateDeleteAPIView

app_name='accessory_history'
urlpatterns = [
    path('list_create/', AccessoryHistoryListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', AccessoryHistoryUpdateDeleteAPIView.as_view(),name='update_delete')
]
