from django.urls import path
from m_event_accessory.api.views import MEventAccessoryListCreateAPIView,MEventAccessoryUpdateDeleteAPIView

app_name='m_event_accessory'
urlpatterns = [
    path('list_create/', MEventAccessoryListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', MEventAccessoryUpdateDeleteAPIView.as_view(),name='update_delete')
]
