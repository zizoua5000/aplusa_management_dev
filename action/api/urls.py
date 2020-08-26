from django.urls import path
from action.api.views import ActionListCreateAPIView,ActionUpdateDeleteAPIView

app_name='action'
urlpatterns = [
    path('list_create/', ActionListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', ActionUpdateDeleteAPIView.as_view(),name='update_delete')
]
