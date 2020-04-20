from django.urls import path
from configuration.api.views import ConfigurationListCreateAPIView,ConfigurationUpdateDeleteAPIView

app_name='configuration'
urlpatterns = [
    path('list_create/', ConfigurationListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', ConfigurationUpdateDeleteAPIView.as_view(),name='update_delete')
]
