from django.urls import path
from event_type.api.views import EventTypeListCreateAPIView,EventTypeUpdateDeleteAPIView

app_name='event_type'
urlpatterns = [
    path('list_create/', EventTypeListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', EventTypeUpdateDeleteAPIView.as_view(),name='update_delete')
]
