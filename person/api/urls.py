from django.urls import path
from person.api.views import PersonListCreateAPIView,PersonUpdateDeleteAPIView

app_name='person'
urlpatterns = [
    path('list_create/', PersonListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', PersonUpdateDeleteAPIView.as_view(),name='update_delete')
]
