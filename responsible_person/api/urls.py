from django.urls import path
from responsible_person.api.views import ResponsiblePersonCreateAPIView,ResponsiblePersonUpdateDeleteAPIView

app_name='responsible_person'
urlpatterns = [
    path('list_create/', ResponsiblePersonListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', ResponsiblePersonUpdateDeleteAPIView.as_view(),name='update_delete')
]
