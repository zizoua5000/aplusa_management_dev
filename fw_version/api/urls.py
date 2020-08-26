from django.urls import path
from fw_version.api.views import FWVersionListCreateAPIView,FWVersionUpdateDeleteAPIView

app_name='fw_version'
urlpatterns = [
    path('list_create/', FWVersionListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', FWVersionUpdateDeleteAPIView.as_view(),name='update_delete')
]
