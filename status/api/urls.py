from django.urls import path
from status.api.views import StatusListCreateAPIView,StatusUpdateDeleteAPIView

app_name='status'
urlpatterns = [
    path('list_create/', StatusListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', StatusUpdateDeleteAPIView.as_view(),name='update_delete')
]
