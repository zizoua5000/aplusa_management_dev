from django.urls import path
from permission.api.views import PermissionListCreateAPIView,PermissionUpdateDeleteAPIView

app_name='permission'
urlpatterns = [
    path('list_create/', PermissionListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', PermissionUpdateDeleteAPIView.as_view(),name='update_delete'),
]
