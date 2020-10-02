from django.urls import path
from simcard_history.api.views import SimcardHistoryListCreateAPIView,SimcardHistoryUpdateDeleteAPIView

app_name='simcard_history'
urlpatterns = [
    path('list_create/', SimcardHistoryListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', SimcardHistoryUpdateDeleteAPIView.as_view(),name='update_delete')
]
