from django.urls import path
from m_event_person.api.views import MEventPersonListCreateAPIView,MEventPersonUpdateDeleteAPIView

app_name='m_event_person'
urlpatterns = [
    path('list_create/', MEventPersonListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', MEventPersonUpdateDeleteAPIView.as_view(),name='update_delete')
]
