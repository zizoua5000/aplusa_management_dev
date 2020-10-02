from django.urls import path
from event.api.views import EventListCreateAPIView,EventUpdateDeleteAPIView

app_name='event'
urlpatterns = [
    path('list_create/', EventListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', EventUpdateDeleteAPIView.as_view(),name='update_delete')
]
