from django.urls import path
from qaime.api.views import QaimeListCreateAPIView,QaimeUpdateDeleteAPIView

app_name='qaime'
urlpatterns = [
    path('list_create/', QaimeListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', QaimeUpdateDeleteAPIView.as_view(),name='update_delete')
]
