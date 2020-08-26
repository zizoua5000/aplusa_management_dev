from django.urls import path
from action_group.api.views import ActionGroupListCreateAPIView,ActionGroupUpdateDeleteAPIView

app_name='action_group'
urlpatterns = [
    path('list_create/', ActionGroupListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', ActionGroupUpdateDeleteAPIView.as_view(),name='update_delete')
]
