from django.urls import path
from pending.api.views import PendingListCreateAPIView,PendingUpdateDeleteAPIView

app_name='pending'
urlpatterns = [
    path('list_create/', PendingListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', PendingUpdateDeleteAPIView.as_view(),name='update_delete')
]
